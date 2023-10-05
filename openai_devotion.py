import langchain

# Create a LangChain object
langchain = langchain.LangChain()

# Set the prompt
prompt = """
Write a devotion based on Psalms 31:1-2, in the same way that I have instructed you:

#IndisputableGeneration
Tuesday 26th September 2023

YOUR DAILY PRAYER IGNITE 
BY Ap. Samuel Muyita

John 12:3 Then took Mary a pound of ointment of spikenard, very costly, and anointed the feet of Jesus, and wiped his feet with her hair: and the house was filled with the odour of the ointment.

SPENDING ON JESUS 

It’s in the ways of God that He only trusts you with what you can give Him back. Anything you aren’t ready to spend on Him, you aren’t ready to receive!

The scriptures are clear, “For where your treasure is, there will your heart be also” Matthew 6:21. Whenever our hearts are fully given to Him, our treasures too will be!

In our theme scripture, we see Mary, taking something very costly and spending it on Jesus! Judas called it wasting, but Jesus saw it as love! She added on that and laid her crown of glory (hair) at the feet of Jesus to wipe His feet!

Whatever we spend on behalf of God is not wasted, but it’s a statement to heaven that we understand where our treasure is, and there our hearts also will be!

Your heart will be tested, God will try you with a little of what you think you are ready for, and oftentimes, many eyes are blinded by the hand of God that they miss His heart. If you can’t spend on behalf of the Kingdom, you’re not yet ready for abundance.

PRAYER POINT 
You have the wisdom to lay down anything for the sake of the Kingdom. You understand the responsibility of wealth and as God multiplies what is upon your life, your heart stays fixed on God as your ultimate treasure. Hallelujah
"""

# Request a response from OpenAI
response = langchain.request(
    model="text-davinci",
    prompt=prompt,
    temperature=0.7,
    max_tokens=1000,
)

# Print the response
print(response)
