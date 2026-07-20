"""
Health analysis service using LangChain and Ollama
"""
import logging
import json
import re
from typing import Dict, List
from langchain_ollama import ChatOllama
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from config import (
    LLM_MODEL,
    LLM_TEMPERATURE,
    LLM_MAX_TOKENS,
    HEALTH_ANALYSIS_PROMPT_TEMPLATE
)

logger = logging.getLogger(__name__)


class HealthAnalysisService:
    """Service for analyzing patient health information using LLM"""
    
    def __init__(self):
        """Initialize the health analysis service"""
        try:
            self.llm = ChatOllama(
                model=LLM_MODEL,
                temperature=LLM_TEMPERATURE,
                base_url="http://localhost:11434"  # Default Ollama server
            )
            logger.info(f"Initialized LLM with model: {LLM_MODEL}")
        except Exception as e:
            logger.error(f"Failed to initialize LLM: {str(e)}")
            raise
    
    def analyze_patient_health(self, patient_data: str) -> Dict:
        """
        Analyze patient health information and provide recommendations
        
        Args:
            patient_data: Patient information as text
            
        Returns:
            Dictionary containing health analysis
        """
        try:
            logger.info("Starting health analysis...")
            
            # Create prompt template
            prompt_template = PromptTemplate(
                input_variables=["patient_data"],
                template=HEALTH_ANALYSIS_PROMPT_TEMPLATE
            )
            
            # Create chain
            chain = prompt_template | self.llm | StrOutputParser()
            
            # Invoke the chain
            response = chain.invoke({"patient_data": patient_data})
            
            logger.info("LLM analysis completed")
            
            # Parse the response
            analysis = self._parse_analysis_response(response)
            
            return analysis
            
        except Exception as e:
            logger.error(f"Error during health analysis: {str(e)}")
            raise
    
    def _parse_analysis_response(self, response: str) -> Dict:
        """
        Parse LLM response into structured format
        
        Args:
            response: Raw LLM response text
            
        Returns:
            Structured analysis dictionary
        """
        analysis = {
            "summary": "",
            "healthy_habits": [],
            "unhealthy_habits": [],
            "recommendations": [],
            "disclaimer": ""
        }
        
        try:
            # Split response into sections
            lines = response.split('\n')
            current_section = None
            
            for line in lines:
                line = line.strip()
                
                if not line:
                    continue
                
                # Detect section headers
                if '**health summary**' in line.lower():
                    current_section = 'summary'
                    continue
                elif '**healthy habits**' in line.lower():
                    current_section = 'healthy_habits'
                    continue
                elif '**areas for improvement**' in line.lower() or '**unhealthy habits**' in line.lower():
                    current_section = 'unhealthy_habits'
                    continue
                elif '**recommendations**' in line.lower():
                    current_section = 'recommendations'
                    continue
                elif '**disclaimer**' in line.lower():
                    current_section = 'disclaimer'
                    continue
                
                # Process line based on current section
                if current_section == 'summary' and not line.startswith('**'):
                    analysis['summary'] += line + ' '
                
                elif current_section == 'healthy_habits' and line.startswith('-'):
                    habit = line.lstrip('- ').strip()
                    if habit:
                        analysis['healthy_habits'].append(habit)
                
                elif current_section == 'unhealthy_habits' and line.startswith('-'):
                    habit = line.lstrip('- ').strip()
                    if habit:
                        analysis['unhealthy_habits'].append(habit)
                
                elif current_section == 'recommendations' and line.startswith('-'):
                    rec = line.lstrip('- ').strip()
                    if rec:
                        analysis['recommendations'].append(rec)
                
                elif current_section == 'disclaimer' and not line.startswith('**'):
                    analysis['disclaimer'] += line + ' '
            
            # Clean up whitespace
            analysis['summary'] = analysis['summary'].strip()
            analysis['disclaimer'] = analysis['disclaimer'].strip()
            
            # Ensure we have valid data
            if not analysis['summary']:
                analysis['summary'] = "Health analysis completed. Please review the detailed findings below."
            
            if not analysis['disclaimer']:
                analysis['disclaimer'] = (
                    "⚠️ Medical Disclaimer: This analysis is for informational purposes only and should not be "
                    "considered as professional medical advice. Always consult with qualified healthcare professionals "
                    "for diagnosis and treatment recommendations."
                )
            
            logger.info(f"Parsed analysis: {len(analysis['healthy_habits'])} healthy, "
                       f"{len(analysis['unhealthy_habits'])} unhealthy habits, "
                       f"{len(analysis['recommendations'])} recommendations")
            
            return analysis
            
        except Exception as e:
            logger.error(f"Error parsing analysis response: {str(e)}")
            # Return analysis with raw response as fallback
            analysis['summary'] = response[:500]
            return analysis
