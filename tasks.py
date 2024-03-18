from crewai import Task
from textwrap import dedent


# This is an example of how to define custom tasks.
# You can define as many tasks as you want.
# You can also define custom agents in agents.py
class CustomTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission! Really appreciate the great work thank you!"

    def linguistic_review_task(self, agent, var1):
        return Task(
            description=dedent(
                f"""
            As a expert Linguistic Reviewer, your task is to scrutinize the English document for its tone, consistency, and style. Pay close attention to the following aspects:
                
                - **Tone:** Ensure that the tone of the document is appropriate for its intended audience and purpose. It should convey the right level of formality, emotion, and engagement.
                
                - **Consistency:** Check for consistency in terminology, voice, and perspective throughout the document. Consistent use of terms and phrases is crucial for clarity and coherence.
                
                - **Style:** Evaluate the document's style, including sentence structure, grammar, and punctuation. The style should be suitable for the document's type and target audience.
                
                Provide detailed feedback on areas for improvement and suggest specific changes to enhance the document's linguistic quality. Your final submission should include a revised version of the document that addresses these aspects
            
            {self.__tip_section()}
    
            Make sure to review carefully and write down all comments and suggestions for improvement in the linguistic_review.md file. Your feedback will help strengthen the document. Let me know if you have any other questions
    
            The English target is located in the following directory {var1}
        """
            ),
            agent=agent,
            output_file='docs/linguistic_review.md',
            expected_output="A document with comments, including adjustments for tone, consistency, and style."  
            
        )

    def cross_checking_task(self, agent, var1, var2):
        return Task(
            description=dedent(
                f"""
            As a Cross-checking Specialist, your primary responsibility is to compare the Korean source document with its English translation. This comparison should focus on the following key areas:

                - **Accuracy:** Ensure that the translation accurately conveys the content and nuances of the original document. Pay special attention to technical terms, idiomatic expressions, and cultural references.

                - **Cultural Appropriateness:** Evaluate the translation for cultural sensitivity and appropriateness. Ensure that cultural nuances are respected and accurately represented in the translation.

                - **Preservation of Original Meaning:** Confirm that the original message, tone, and intent of the source document are preserved in the translation. Adjustments may be necessary to ensure the translation remains true to the source while being understandable to the English-speaking audience.

                Document your findings and provide specific recommendations for adjustments where necessary. Your feedback should include examples from the text where improvements are needed and suggest how these sections can be revised to meet the above criteria.
                                       
            {self.__tip_section()}

            Make sure to review carefully and cross-check thoroughly between the Korean source document and its English translation. Pay close attention to any discrepancies in technical terminology, cultural references, numbers.

            The English target to cross-check is located in the following directory {var1}
            The original Korean source document is in {var2}

        """
            ),
            agent=agent,
            output_file='docs/cross_review.md',
            expected_output="A document with comments post cross check, including adjustments for tone, consistency, and style."  
            
        )
    
    def final_review_task(self, agent, var1, var2):
        return Task(
            description=dedent(f"""\
                As the Final Review Expert, your task is to perform the last comprehensive review of the document, integrating feedback from both the Linguistic Reviewer and the Cross-checking Specialist. Focus on the following aspects:

                - **Overall Quality:** Ensure that the document meets the highest standards of quality, including accuracy, clarity, and professional presentation.
                
                - **Coherence and Unity:** Assess the document for coherence, ensuring that all parts work together seamlessly and that the document reads as a unified whole.
                
                - **Feedback Integration:** Confirm that feedback and suggested changes from previous reviews have been effectively incorporated into the document.
                
                - **Readiness for Delivery:** Verify that the document is free of errors and is in the best possible form for delivery to the customer.

                Your review should culminate in a final version of the document that addresses all concerns and is polished to meet professional standards. Provide a brief report summarizing the changes made and affirming the document's readiness for delivery.
                               
                The English target to cross-check is located in the following directory {var1}
                The original Korean source document is in {var2}
                Use docs/linguistic_review.md if available. Otherwise use docs/cross_review.md.
                               
                """),
            agent=agent,
            output_file='docs/final_translation.md',
            expected_output="final english target translation based on review and cross-check."  
        )
    
    def final_edit(self, agent, var1, var2):
        return Task(
            description=dedent(f"""\
                As the Final Review Expert, your task is to perform the last comprehensive review of the document, integrating feedback from both the Linguistic Reviewer and the Cross-checking Specialist. Focus on the following aspects:

                - **Overall Quality:** Ensure that the document meets the highest standards of quality, including accuracy, clarity, and professional presentation.
                
                - **Coherence and Unity:** Assess the document for coherence, ensuring that all parts work together seamlessly and that the document reads as a unified whole.
                
                - **Feedback Integration:** Confirm that feedback and suggested changes from previous reviews have been effectively incorporated into the document.
                
                - **Readiness for Delivery:** Verify that the document is free of errors and is in the best possible form for delivery to the customer.

                Your review should culminate in a final version of the document that addresses all concerns and is polished to meet professional standards. Provide a brief report summarizing the changes made and affirming the document's readiness for delivery.
                               
                The English target to cross-check is located in the following directory {var1}
         Based on docs/linguistic_review.md and docs/cross_review.md,
                Provide final edits to the translation based on reviews in the specified files. Export the final edited translation to docs/final_translation.md 
                               
                """),
            agent=agent,
            output_file='docs/final_translation.md',
            expected_output="final edit of translation based on comments."  
        )
    
   