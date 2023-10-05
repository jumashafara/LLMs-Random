import requests

# Replace with your API token
API_TOKEN = "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"

# Set the URL for the API call
url = f"https://api.huggingface.co/api/v1/models/bert-base-uncased/generate"

# Define the headers for the API call
headers = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}

# Define the payload for the API call


text = '''Smoke from hundreds of wildfires in Canada is triggering air quality alerts throughout the US. Skylines from Maine to Maryland to Minnesota are gray and smoggy. And in some places, the air quality warnings include the warning to stay inside. We wanted to better understand what's happening here and why, so we called Peter DiCarlo, an associate professor in the Department of Environmental Health and Engineering at Johns Hopkins University. Good morning, professor. Good morning. So what is it about the conditions right now that have caused this round of wildfires to affect so many people so far away? Well, there's a couple of things. The season has been pretty dry already, and then the fact that we're getting hit in the US. Is because there's a couple of weather systems that are essentially channeling the smoke from those Canadian wildfires through Pennsylvania into the Mid Atlantic and the Northeast and kind of just dropping the smoke there. So what is it in this haze that makes it harmful? And I'm assuming it is is it is the levels outside right now in Baltimore are considered unhealthy. And most of that is due to what's called particulate matter, which are tiny particles, microscopic smaller than the width of your hair, that can get into your lungs and impact your respiratory system, your cardiovascular system, and even your neurological your brain. What makes this particularly harmful? Is it the volume of particulate? Is it something in particular? What is it exactly? Can you just drill down on that a little bit more? Yeah. So the concentration of particulate matter I was looking at some of the monitors 
that we have was reaching levels of what are, in science speak, 150 micrograms per meter cubed, 
which is more than ten times what the annual average should be, and about four times higher than what you're supposed to have on a 24 hours average. And so the concentrations of these particles in the air are just much, much higher than we typically see. And exposure to those high levels can lead to a host of health problems. And who is most vulnerable? I noticed that in New York City, for example, they're canceling outdoor activities, and so here it is in the early days of summer, and they have to keep all the kids inside. So who tends to be vulnerable in a situation like this? It's the youngest. So children, obviously, whose bodies are still developing. The elderly who know their bodies are more in decline, and they're more susceptible to the health impacts of breathing, the poor air quality. And then people who have preexisting health conditions, people with respiratory conditions or heart conditions can be triggered by high levels of air pollution. Could this get worse? That's a good in some areas, it's much worse than others. And it just depends on kind of where the smoke is concentrated. I think New York has some of the higher concentrations right now, but that's going to change as that air moves away from the New York area. But over the course of the next few days, we will see different areas being hit at different 
times with the highest concentrations. I was going to ask you, more fires start burning, I don't expect the concentrations to go up too much higher. I was going to ask you and you started to answer this, but how much longer could this last? Or forgive me if I'm asking you to speculate, but what do you think? Well, I think the fires are going to burn for a little bit longer, but the key for us in the US. Is the weather system changing. And so right now, it's kind of the weather systems that are pulling that air into our mid Atlantic and Northeast region. As those weather systems change and shift, we'll see that smoke going elsewhere and not impact us in this region as much. And so I think that's going to be the defining factor. And I think the next couple of 
days we're going to see a shift in that weather pattern and start to push the smoke away from where we are. And finally, with the impacts of climate change, we are seeing more wildfires. Will 
we be seeing more of these kinds of wide ranging air quality consequences or circumstances? I mean, that is one of the predictions for climate change. Looking into the future, the fire season 
is starting earlier and lasting longer and we're seeing more frequent fires. So, yeah, this is probably something that we'll be seeing more frequently. This tends to be much more of an issue in the Western US. So the Eastern US getting hit right now is a little bit new. But yeah, I think with climate change moving forward, this is something that is going to happen more frequently. 
That's Peter DiCarlo, associate professor in the Department of Environmental Health and Engineering at Johns Hopkins University. Sergeant Carlo, thanks so much for joining us and sharing this 
expertise with us. Thank you for having me.'''
payload = {
    "inputs": [text],
    "instructions": "summarize",
    "max_length": 50,
    "temperature": 0.7,
    "top_k": 4,
    "frequency_threshold": 0.3
}

# Make the API call
response = requests.post(url, headers=headers, json=payload)

# Check the response status code
if response.status_code == 200:
    # Print the summary
    print(response.json()["output"])
else:
    # Print the error message
    print(f"Error: {response.status_code} {response.reason}")