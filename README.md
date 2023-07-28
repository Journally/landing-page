# Journally - A journal entry a day. All through text.
## :star: :pencil2: :pencil: :gift:

## Welcome to Journally's Landing Page
<img width="1287" alt="UpdatedLandingPage" src="https://github.com/Journally/landing-page/assets/68709672/64bf0fff-fed7-48b6-9a66-cd2e4d32bc68">

## Learn more about Journally
Welcome to Journally! Where we restore our memories one journal, one day at a time. Journally sends you a daily reminder via text, where you respond by writing a short journal, where you can access these journals later on the Journally website.

[Quick Demo Video](https://www.youtube.com/watch?v=Z_z_92_XajY&t=3s)

### View our full repo
[Journally Repo](https://github.com/Journally/journally)

## :books: Technologies :books:
* **Twilio** to send our registered users *daily* messages to Journal!
* Secure `MySQL` database to to store user registration info and their journally entries
* `Flask` to *send* SMS from a user database of phone numbers
* `Flask` to *receive* SMS and store the user's Journallys into the database
* `Node.JS` for server routings, user registration on site, and storing user data into the database
* `Express.js` backend to host Journally
* `Bootstrap` for footers and buttons and a *responsive design*

## Deployment - Rough Steps
1. Download the Google Cloud CLI: `https://cloud.google.com/sdk/docs/install`
2. You should link the local CLI with the journally account
3. `gcloud config set project journally-landing-page`
4. `gcloud app deploy`
5. The bottom instruction was already done:
- Add app engine deployer permission here:
- https://console.cloud.google.com/iam-admin/iam?orgonly=true&project=journally-landing-page&supportedpurview=organizationId,folder,project
