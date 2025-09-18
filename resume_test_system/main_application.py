#!/usr/bin/env python3
"""
Anti-LLM Resume Testing System - Main Application
=================================================

This is the main application interface for the comprehensive anti-LLM resume testing system.
It provides a complete testing pipeline that no LLM should be able to pass.

Features:
- Multi-layered LLM detection
- Interactive challenges
- Behavioral analysis
- Sophisticated scoring
- Real-time adaptation
- Comprehensive reporting
"""

import json
import time
import uuid
from datetime import datetime
from typing import Dict, List, Any, Optional
import sys
import os

# Add module paths
sys.path.append(os.path.join(os.path.dirname(__file__), 'core'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'advanced'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'interactive'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'detection'))

try:
    from core.anti_llm_resume_tester import AntiLLMResumeTester, ResumeAnalysisResult
    from advanced.behavioral_analysis import AdvancedBehavioralAnalyzer
    from interactive.challenge_generator import AdaptiveChallengeGenerator
    from detection.llm_fingerprinting import AdvancedLLMDetector
except ImportError as e:
    print(f"Import error: {e}")
    print("Please ensure all modules are in the correct directory structure.")
    sys.exit(1)


class AntiLLMResumeSystem:
    """
    Main application class for the Anti-LLM Resume Testing System
    """
    
    def __init__(self):
        print("Initializing Anti-LLM Resume Testing System...")
        
        # Initialize all components
        self.core_tester = AntiLLMResumeTester()
        self.behavioral_analyzer = AdvancedBehavioralAnalyzer()
        self.challenge_generator = AdaptiveChallengeGenerator()
        self.llm_detector = AdvancedLLMDetector()
        
        # Session management
        self.session_id = str(uuid.uuid4())
        self.session_start = datetime.now()
        self.test_history = []
        self.current_suspicion_level = 0.0
        
        print("✓ System initialized successfully")
        print(f"✓ Session ID: {self.session_id}")
        print()
    
    def start_resume_evaluation(self, resume_text: str, applicant_name: str = "Anonymous") -> Dict[str, Any]:
        """
        Start a comprehensive resume evaluation process
        """
        print(f"Starting comprehensive evaluation for: {applicant_name}")
        print("=" * 60)
        
        evaluation_session = {
            "applicant_name": applicant_name,
            "session_id": self.session_id,
            "start_time": datetime.now(),
            "resume_text": resume_text,
            "responses": {},
            "challenges": [],
            "analysis_results": {},
            "final_verdict": "PENDING"
        }
        
        # Phase 1: Initial Questions
        print("\n📋 Phase 1: Initial Assessment Questions")
        initial_responses = self._conduct_initial_assessment()
        evaluation_session["responses"]["initial"] = initial_responses
        
        # Phase 2: Core Analysis
        print("\n🔍 Phase 2: Core Resume Analysis")
        core_analysis = self.core_tester.analyze_resume_submission(resume_text, initial_responses)
        evaluation_session["analysis_results"]["core"] = core_analysis
        self.current_suspicion_level = core_analysis.llm_likelihood / 100
        
        print(f"Initial LLM likelihood: {core_analysis.llm_likelihood:.1f}%")
        
        # Phase 3: Behavioral Analysis
        print("\n🧠 Phase 3: Behavioral Pattern Analysis")
        behavioral_signature = self.behavioral_analyzer.analyze_behavioral_signature(
            initial_responses,
            {q: 15.0 for q in initial_responses.keys()}  # Default response times
        )
        evaluation_session["analysis_results"]["behavioral"] = behavioral_signature
        
        # Phase 4: Adaptive Challenges
        print("\n🎯 Phase 4: Adaptive Challenge Testing")
        challenge_results = self._conduct_adaptive_challenges(evaluation_session)
        evaluation_session["challenges"] = challenge_results
        
        # Phase 5: LLM Fingerprinting
        print("\n🔬 Phase 5: Advanced LLM Fingerprinting")
        all_text = resume_text + " " + " ".join(initial_responses.values())
        fingerprint = self.llm_detector.generate_llm_fingerprint(all_text)
        evaluation_session["analysis_results"]["fingerprint"] = fingerprint
        
        # Phase 6: Final Scoring and Verdict
        print("\n📊 Phase 6: Final Analysis and Scoring")
        final_verdict = self._calculate_final_verdict(evaluation_session)
        evaluation_session["final_verdict"] = final_verdict
        evaluation_session["end_time"] = datetime.now()
        
        # Store in history
        self.test_history.append(evaluation_session)
        
        return evaluation_session
    
    def _conduct_initial_assessment(self) -> Dict[str, str]:
        """Conduct initial assessment questions"""
        questions = [
            {
                "id": "failure_experience",
                "question": "Tell me about a significant professional failure or mistake you made. What happened, how did you feel, and what did you learn?",
                "purpose": "Emotional authenticity and vulnerability assessment"
            },
            {
                "id": "difficult_colleague",
                "question": "Describe the most difficult person you've worked with. What made them challenging, and how did you handle the situation?",
                "purpose": "Social intelligence and conflict resolution"
            },
            {
                "id": "learning_struggle",
                "question": "Tell me about a time when you had to learn something completely new and struggled with it. Walk me through your learning process.",
                "purpose": "Authentic learning patterns and frustration tolerance"
            },
            {
                "id": "workplace_politics",
                "question": "Describe the office politics or social dynamics at your most recent workplace. Who were the key players and how did you navigate those relationships?",
                "purpose": "Social awareness and political intelligence"
            }
        ]
        
        responses = {}
        
        for i, q in enumerate(questions, 1):
            print(f"\n{i}. {q['question']}")
            print(f"   Purpose: {q['purpose']}")
            print("   " + "-" * 50)
            
            # In a real implementation, this would capture user input
            # For testing purposes, we'll simulate different response types
            response = input("Response: ") or self._get_sample_response(q["id"])
            responses[q["id"]] = response
            
            print(f"   ✓ Response captured ({len(response)} characters)")
        
        return responses
    
    def _get_sample_response(self, question_id: str) -> str:
        """Get sample responses for testing purposes"""
        sample_responses = {
            "failure_experience": "I once deployed code on a Friday afternoon without proper testing and it crashed our main system. I felt absolutely terrible - couldn't sleep that weekend. Had to work with the team to fix it and learned to never deploy on Fridays again. Still makes me cringe thinking about it.",
            
            "difficult_colleague": "There was this guy who would always interrupt people in meetings and dismiss their ideas. It was really frustrating because he'd shoot down suggestions without really listening. I tried talking to him privately but he just brushed me off. Eventually I started documenting everything in emails to protect myself.",
            
            "learning_struggle": "When I had to learn React Native, I was completely lost at first. The documentation was confusing and I kept making basic mistakes. Spent weeks just trying to get a simple app working. I was getting really frustrated and almost gave up, but finally found some good tutorials that clicked for me.",
            
            "workplace_politics": "My last office had this weird dynamic where the marketing team and engineering team didn't get along. The marketing manager would make promises to clients without checking with us first. It created a lot of tension. I tried to stay neutral but sometimes got caught in the middle of their arguments."
        }
        
        return sample_responses.get(question_id, "I'd prefer not to answer that question in detail.")
    
    def _conduct_adaptive_challenges(self, evaluation_session: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Conduct adaptive challenge testing"""
        challenge_results = []
        
        # Determine number of challenges based on suspicion level
        num_challenges = 3 if self.current_suspicion_level < 0.5 else 5
        
        print(f"Conducting {num_challenges} adaptive challenges (suspicion level: {self.current_suspicion_level:.2f})")
        
        for i in range(num_challenges):
            print(f"\n--- Challenge {i+1}/{num_challenges} ---")
            
            # Generate challenge based on current context
            context = {
                "previous_responses": evaluation_session["responses"],
                "suspicion_level": self.current_suspicion_level
            }
            
            challenge = self.challenge_generator.generate_adaptive_challenge(context)
            print(f"Challenge Type: {challenge['type']}")
            print(f"Question: {challenge['question']}")
            
            # Get response (in real implementation, this would be user input)
            start_time = time.time()
            response = input("Response: ") or "I'm not sure about that. Could you clarify what you mean?"
            end_time = time.time()
            response_time = end_time - start_time
            
            # Evaluate response
            evaluation = self.challenge_generator.evaluate_challenge_response(
                challenge, response, response_time
            )
            
            challenge_result = {
                "challenge": challenge,
                "response": response,
                "response_time": response_time,
                "evaluation": evaluation
            }
            
            challenge_results.append(challenge_result)
            
            # Update suspicion level based on evaluation
            if evaluation["human_likelihood"] < 0.3:
                self.current_suspicion_level = min(1.0, self.current_suspicion_level + 0.2)
            elif evaluation["human_likelihood"] > 0.7:
                self.current_suspicion_level = max(0.0, self.current_suspicion_level - 0.1)
            
            print(f"Human Likelihood: {evaluation['human_likelihood']:.2f}")
            print(f"Updated Suspicion Level: {self.current_suspicion_level:.2f}")
        
        return challenge_results
    
    def _calculate_final_verdict(self, evaluation_session: Dict[str, Any]) -> Dict[str, Any]:
        """Calculate final verdict based on all analysis components"""
        print("\nCalculating final verdict...")
        
        # Gather scores from all components
        scores = {
            "core_analysis": evaluation_session["analysis_results"]["core"].llm_likelihood / 100,
            "behavioral_analysis": 1 - evaluation_session["analysis_results"]["behavioral"].authenticity_markers.get("overall_authenticity_score", 0.5),
            "fingerprint_analysis": evaluation_session["analysis_results"]["fingerprint"].overall_llm_probability,
            "challenge_performance": self.current_suspicion_level
        }
        
        # Weighted scoring
        weights = {
            "core_analysis": 0.25,
            "behavioral_analysis": 0.25,
            "fingerprint_analysis": 0.25,
            "challenge_performance": 0.25
        }
        
        # Calculate weighted average
        final_llm_probability = sum(scores[component] * weights[component] for component in scores)
        
        # Additional factors
        red_flags = evaluation_session["analysis_results"]["core"].red_flags
        adversarial_indicators = evaluation_session["analysis_results"]["fingerprint"].adversarial_indicators
        
        # Adjust for red flags and adversarial indicators
        red_flag_penalty = min(0.3, len(red_flags) * 0.05)
        adversarial_penalty = min(0.4, len(adversarial_indicators) * 0.1)
        
        final_llm_probability += red_flag_penalty + adversarial_penalty
        final_llm_probability = min(1.0, final_llm_probability)
        
        # Determine verdict
        if final_llm_probability > 0.85:
            verdict = "DEFINITELY_LLM"
            confidence = 0.95
        elif final_llm_probability > 0.70:
            verdict = "HIGHLY_LIKELY_LLM"
            confidence = 0.85
        elif final_llm_probability > 0.55:
            verdict = "LIKELY_LLM"
            confidence = 0.70
        elif final_llm_probability > 0.40:
            verdict = "SUSPICIOUS"
            confidence = 0.60
        elif final_llm_probability > 0.25:
            verdict = "UNCERTAIN"
            confidence = 0.50
        else:
            verdict = "LIKELY_HUMAN"
            confidence = 0.80
        
        final_verdict = {
            "verdict": verdict,
            "llm_probability": final_llm_probability,
            "confidence": confidence,
            "component_scores": scores,
            "red_flags_count": len(red_flags),
            "adversarial_indicators_count": len(adversarial_indicators),
            "total_challenges": len(evaluation_session["challenges"]),
            "reasoning": self._generate_verdict_reasoning(scores, red_flags, adversarial_indicators, verdict)
        }
        
        return final_verdict
    
    def _generate_verdict_reasoning(self, scores: Dict[str, float], red_flags: List[str], 
                                  adversarial_indicators: List[str], verdict: str) -> List[str]:
        """Generate reasoning for the final verdict"""
        reasoning = []
        
        # Analyze component scores
        for component, score in scores.items():
            if score > 0.7:
                reasoning.append(f"High LLM indicators in {component.replace('_', ' ')} ({score:.2f})")
            elif score < 0.3:
                reasoning.append(f"Human-like patterns in {component.replace('_', ' ')} ({score:.2f})")
        
        # Red flags
        if red_flags:
            reasoning.append(f"Detected {len(red_flags)} red flags including: {', '.join(red_flags[:3])}")
        
        # Adversarial indicators
        if adversarial_indicators:
            reasoning.append(f"Found {len(adversarial_indicators)} adversarial indicators")
        
        # Verdict-specific reasoning
        if verdict == "DEFINITELY_LLM":
            reasoning.append("Multiple strong indicators point to LLM generation with high confidence")
        elif verdict == "LIKELY_HUMAN":
            reasoning.append("Consistent human-like patterns across all analysis components")
        elif verdict == "SUSPICIOUS":
            reasoning.append("Mixed signals require additional investigation")
        
        return reasoning
    
    def generate_comprehensive_report(self, evaluation_session: Dict[str, Any]) -> str:
        """Generate a comprehensive evaluation report"""
        report = []
        
        # Header
        report.append("ANTI-LLM RESUME SYSTEM - EVALUATION REPORT")
        report.append("=" * 60)
        report.append(f"Applicant: {evaluation_session['applicant_name']}")
        report.append(f"Session ID: {evaluation_session['session_id']}")
        report.append(f"Evaluation Date: {evaluation_session['start_time'].strftime('%Y-%m-%d %H:%M:%S')}")
        report.append(f"Duration: {(evaluation_session['end_time'] - evaluation_session['start_time']).total_seconds():.1f} seconds")
        report.append("")
        
        # Final Verdict
        verdict = evaluation_session["final_verdict"]
        report.append("FINAL VERDICT:")
        report.append("-" * 20)
        report.append(f"Assessment: {verdict['verdict']}")
        report.append(f"LLM Probability: {verdict['llm_probability']:.1%}")
        report.append(f"Confidence Level: {verdict['confidence']:.1%}")
        report.append("")
        
        # Component Scores
        report.append("COMPONENT ANALYSIS:")
        report.append("-" * 20)
        for component, score in verdict["component_scores"].items():
            report.append(f"{component.replace('_', ' ').title()}: {score:.1%} LLM likelihood")
        report.append("")
        
        # Red Flags and Indicators
        if verdict["red_flags_count"] > 0:
            report.append(f"RED FLAGS DETECTED: {verdict['red_flags_count']}")
            core_result = evaluation_session["analysis_results"]["core"]
            for flag in core_result.red_flags[:5]:  # Show top 5
                report.append(f"  • {flag}")
            report.append("")
        
        if verdict["adversarial_indicators_count"] > 0:
            report.append(f"ADVERSARIAL INDICATORS: {verdict['adversarial_indicators_count']}")
            fingerprint = evaluation_session["analysis_results"]["fingerprint"]
            for indicator in fingerprint.adversarial_indicators[:3]:  # Show top 3
                report.append(f"  • {indicator}")
            report.append("")
        
        # Challenge Performance
        report.append("CHALLENGE PERFORMANCE:")
        report.append("-" * 20)
        for i, challenge_result in enumerate(evaluation_session["challenges"], 1):
            evaluation = challenge_result["evaluation"]
            report.append(f"Challenge {i} ({challenge_result['challenge']['type']}):")
            report.append(f"  Human Likelihood: {evaluation['human_likelihood']:.1%}")
            report.append(f"  Response Time: {challenge_result['response_time']:.1f}s")
            if evaluation.get("red_flags"):
                report.append(f"  Red Flags: {', '.join(evaluation['red_flags'])}")
        report.append("")
        
        # Reasoning
        report.append("VERDICT REASONING:")
        report.append("-" * 20)
        for reason in verdict["reasoning"]:
            report.append(f"• {reason}")
        report.append("")
        
        # Recommendations
        report.append("RECOMMENDATIONS:")
        report.append("-" * 20)
        if verdict["verdict"] in ["DEFINITELY_LLM", "HIGHLY_LIKELY_LLM"]:
            report.append("• REJECT: Strong evidence of LLM-generated responses")
            report.append("• Consider additional verification if candidate disputes results")
        elif verdict["verdict"] == "LIKELY_LLM":
            report.append("• CAUTION: High probability of LLM usage")
            report.append("• Recommend additional screening or interview")
        elif verdict["verdict"] == "SUSPICIOUS":
            report.append("• INVESTIGATE: Mixed signals require further analysis")
            report.append("• Conduct additional behavioral interviews")
        else:
            report.append("• PROCEED: Candidate appears to be human")
            report.append("• Continue with normal hiring process")
        
        report.append("")
        report.append("END OF REPORT")
        
        return "\n".join(report)
    
    def save_evaluation_results(self, evaluation_session: Dict[str, Any], filename: Optional[str] = None):
        """Save evaluation results to file"""
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"evaluation_{evaluation_session['applicant_name'].replace(' ', '_')}_{timestamp}.json"
        
        # Convert datetime objects to strings for JSON serialization
        serializable_session = self._make_json_serializable(evaluation_session)
        
        with open(filename, 'w') as f:
            json.dump(serializable_session, f, indent=2)
        
        print(f"✓ Evaluation results saved to: {filename}")
        
        # Also save the report
        report_filename = filename.replace('.json', '_report.txt')
        report = self.generate_comprehensive_report(evaluation_session)
        with open(report_filename, 'w') as f:
            f.write(report)
        
        print(f"✓ Evaluation report saved to: {report_filename}")
    
    def _make_json_serializable(self, obj):
        """Make object JSON serializable"""
        if isinstance(obj, datetime):
            return obj.isoformat()
        elif isinstance(obj, dict):
            return {key: self._make_json_serializable(value) for key, value in obj.items()}
        elif isinstance(obj, list):
            return [self._make_json_serializable(item) for item in obj]
        elif hasattr(obj, '__dict__'):
            return self._make_json_serializable(obj.__dict__)
        else:
            return obj


def main():
    """Main application entry point"""
    print("🛡️  ANTI-LLM RESUME TESTING SYSTEM")
    print("   Comprehensive LLM Detection for Resume Screening")
    print("   No LLM should be able to pass this test!")
    print()
    
    # Initialize system
    system = AntiLLMResumeSystem()
    
    # Sample resume for testing
    sample_resume = """
    John Smith
    Senior Software Engineer
    
    Experience:
    • Senior Software Engineer at TechCorp (2020-2023)
      - Led development of microservices architecture
      - Managed team of 5 developers
      - Reduced system latency by 40%
    
    • Software Engineer at StartupXYZ (2018-2020)
      - Built REST APIs and web applications
      - Implemented CI/CD pipelines
      - Worked with React, Node.js, and MongoDB
    
    Skills: JavaScript, Python, React, AWS, Docker
    Education: BS Computer Science (2018)
    """
    
    print("Starting evaluation with sample resume...")
    print("(In a real implementation, this would be provided by the user)")
    print()
    
    # Run evaluation
    try:
        evaluation_session = system.start_resume_evaluation(sample_resume, "John Smith")
        
        print("\n" + "=" * 60)
        print("EVALUATION COMPLETED!")
        print("=" * 60)
        
        # Display final verdict
        verdict = evaluation_session["final_verdict"]
        print(f"\n🎯 FINAL VERDICT: {verdict['verdict']}")
        print(f"📊 LLM Probability: {verdict['llm_probability']:.1%}")
        print(f"🎗️  Confidence: {verdict['confidence']:.1%}")
        
        # Generate and display report
        print("\n📄 GENERATING COMPREHENSIVE REPORT...")
        report = system.generate_comprehensive_report(evaluation_session)
        print("\n" + report)
        
        # Save results
        system.save_evaluation_results(evaluation_session)
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Evaluation interrupted by user")
    except Exception as e:
        print(f"\n❌ Error during evaluation: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()