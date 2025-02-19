#🌦️ Weather Alert 🚀
- This Weather Alert Application uses the Twilio API 📲 to send SMS notifications about the weather.
- It fetches a 5-day weather forecast ⛅ with 3-hour intervals using the OpenWeatherMap API 🌍.
- If rain is expected (☔ Carry an umbrella!), or if it's sunny (☀️ No umbrella needed!), the user gets an instant SMS alert.
- 🛠️ How It Works
  
🔹 Step 1: Get API Access

✅ Register with OpenWeatherMap to obtain an API Key 🔑.

✅ Use the 5-day/3-hour forecast API 🌤️.

🔹 Step 2: Fetch Weather Data
✅ Use the requests module to send an API request.

✅ Add latitude & longitude 🌍 (use latlong.net to find yours).

✅ Handle exceptions using raise_for_status().

✅ Convert the response into JSON format 📜.

🔹 Step 3: Analyze Weather Conditions
✅ Loop through the JSON response to extract weather conditions.

✅ Use OpenWeatherMap's weather condition codes (Reference).

✅ If the weather ID is less than 700, it indicates rainy weather ☔.

🔹 Step 4: Send Weather Alerts
✅ Print whether it will rain or be sunny.

✅ Convert this message into an SMS alert using Twilio.

🔹 Step 5: Setup Twilio for SMS
✅ Sign up for Twilio 🔹 to get:
auth_token 🔐
account_sid 🆔

✅ Get a Twilio phone number 📱 to send alerts.

✅ Use the client.messages.create() method to send SMS.

🔹 Step 6: Automate with PythonAnywhere

✅ Upload the script to PythonAnywhere 💻.

✅ Since a free account lacks a dedicated server, configure a proxy server using TwilioHttpClient.

✅ Modify the Twilio client connection to use http_client=proxy_client.

🔹 Step 7 (Optional): Secure Credentials 🔒.
✅ Use environment variables to hide sensitive information:

export YOUR_API_KEY

export YOUR_AUTH_TOKEN

export YOUR_ACCOUNT_SID

✅ Replace hardcoded values with os.environ.get("YOUR_API_KEY").

✅ Automate the script by adding the following to PythonAnywhere tasks:

export YOUR_API_KEY; export YOUR_AUTH_TOKEN; export YOUR_ACCOUNT_SID; python3 main.py

✅ Now, you’ll receive daily weather alerts automatically! 🎉
