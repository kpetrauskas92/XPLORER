# EXPLORER

## Introduction

XPLORER is a social media platform built using Django, JavaScript, CSS, and HTML. It's a space for users to share their experiences, photos, and stories with others from all over the world. Whether you want to show off a great spot you visited, share a personal thought, or give a recommendation, XPLORER is the place to do it.

This platform is a project for the Code Institute Diploma in Software Development with eCommerce. On XPLORER, users can sign up, and create, edit, or delete their own posts and comments. They can also set up and manage their personal profiles. Join XPLORER and connect with a community eager to share and explore.

![Screenshot of homepage](media/readme/landing.gif)

[View the live website on Heroku](https://xplorer-p4-ad2c5b0b95ce.herokuapp.com)

Please note: To open any links in this document in a new browser tab, please press CTRL + Click.

## Table of Contents

* [User Experience Design (UX)](#ux)
  * [The Strategy Plane](#the-strategy-plane)
    * [Site Goals](#site-goals)
    * [Epics](#epics)
    * [User Stories](#user-stories)
  * [The Scope Plane](#the-scope-plane)
  * [The Structure Plane](#the-structure-plane)
    * [Opportunities](#opportunities)
  * [The Skeleton Plane](#the-skeleton-plane)
    * [Wireframes](#Wireframe-mockups)
    * [Database Schema](#database-schema)
  * [The Surface Plane](#the-surface-plane)
* [Features](#features)
* [Future Enhancements](#future-enhancements)
* [Technologies Used](#technologies-used)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)

## UX

### The Strategy Plane

* XPLORER is designed to be a welcoming online hub where users can share, discover, and engage with intriguing experiences and adventures. Not only can members dive into stories shared by peers from every corner of the globe, but they can also show their appreciation by liking or unliking posts. Want to stay updated with your favorite XPLORER storytellers? Simply follow other users to get their latest tales right in your feed.

#### The Sites Ideal User

* Someone who is passionate about sharing their unique travels and experiences.
* Someone who wants to expand their knowledge of global stories, adventures, and local experiences.
* Someone who draws inspiration from the shared stories.
* Someone eager to grow their online presence by consistently sharing, engaging.

#### Site Goals

* To provide users with a platform to share their unique adventures and stories.
* To provide users with a space to connect with and follow fellow explorers.
* To provide users with a hub to draw inspiration from diverse experiences around the world.

#### Epics

**10 Epics** were created which were then further developed into 31 User Stories. The details on each epic, along with the user stories linked to each one can be found in the project kanban board [here](https://github.com/users/kpetrauskas92/projects/1)

1. User Registration [#1](https://github.com/kpetrauskas92/XPLORER/issues/1)
2. User Login [#2](https://github.com/kpetrauskas92/XPLORER/issues/2)
3. User Profile [#3](https://github.com/kpetrauskas92/XPLORER/issues/3)
4. Post Creation [#4](https://github.com/kpetrauskas92/XPLORER/issues/4)
5. Like Posts & Comments [#5](https://github.com/kpetrauskas92/XPLORER/issues/5)
6. Comment Reply [#6](https://github.com/kpetrauskas92/XPLORER/issues/55)
7. News Feed [#7](https://github.com/kpetrauskas92/XPLORER/issues/6)
8. User Follow/Unfollow [#8](https://github.com/kpetrauskas92/XPLORER/issues/7)
9. User Search [#9](https://github.com/kpetrauskas92/XPLORER/issues/8)
10. User Logout [#10](https://github.com/kpetrauskas92/XPLORER/issues/11)

### User Stories

From the Epics, 31 User stories were developed. Each story was assigned a classification of Must-Have, Should-Have, Could-Have or Won't Have. The full list of User Stories, seperated by those completed and those pushed to a future release is available on the project [kanban board](https://github.com/users/kpetrauskas92/projects/1).

These are the user stories that were completed within the projects first release, by EPIC.

### **1. User Registration**

* USER STORY [#26](https://github.com/kpetrauskas92/XPLORER/issues/26)

    Basic Registration
  * As a new user, I want to register for an account so that I can access the platform's features.

* USER STORY [#28](https://github.com/kpetrauskas92/XPLORER/issues/28)

    Verification
  * As a registered user, I want my profile to be verified so that other users can trust the authenticity of my profile.

* USER STORY [#29](https://github.com/kpetrauskas92/XPLORER/issues/29)

    Social Media Integration
  * As a user, I want to register on the platform using my social media accounts so that I can simplify the sign-up process and quickly join the community.

### **2. User Login**

* USER STORY [#30](https://github.com/kpetrauskas92/XPLORER/issues/30)

    Standard Login
  * As a registered user, I want to log in using my username/email and password so that I can securely access my account.

* USER STORY [#31](https://github.com/kpetrauskas92/XPLORER/issues/31)

    Forgotten Password
  * As a user who has forgotten my password, I want to reset it so that I can regain access to my account.

* USER STORY [#32](https://github.com/kpetrauskas92/XPLORER/issues/32)

    Remember Me Option
  * As a user logging in, I want the platform to remember my session so that I don't have to log in every time I visit.

### **3. User Login**

* USER STORY [#33](https://github.com/kpetrauskas92/XPLORER/issues/33)

    Viewing Profile
  * As a registered user, I want to log in using my username/email and password so that I can securely access my account.

* USER STORY [#34](https://github.com/kpetrauskas92/XPLORER/issues/34)

    Editing Profile Details
  * As a registered user, I want to edit my profile information so that I can keep my details up-to-date.

* USER STORY [#35](https://github.com/kpetrauskas92/XPLORER/issues/35)

    Changing Profile Picture
  * As a registered user, I want to change my profile picture so that I can personalize my profile.

* USER STORY [#36](https://github.com/kpetrauskas92/XPLORER/issues/36)

    Setting Profile Preferences
  * As a registered user, I want to set preferences in my profile so that I can customize my experience on the platform.

* USER STORY [#40](https://github.com/kpetrauskas92/XPLORER/issues/40)

    Profile Deletion
  * As a registered user, I want to delete my profile so that my data and activities are permanently removed from the platform.

### **4. Post Creation**

* USER STORY [#37](https://github.com/kpetrauskas92/XPLORER/issues/37)

    Basic Post Creation
  * As a user, I want to create a post so that I can share content with others on the platform.

* USER STORY [#38](https://github.com/kpetrauskas92/XPLORER/issues/38)

    Adding Images to Post
  * As a user, I want to add images to my post so that my content can be more engaging and descriptive.

* USER STORY [#39](https://github.com/kpetrauskas92/XPLORER/issues/39)

    Tagging in Posts
  * As a user, I want to add tags to my post so that it can be more discoverable to users interested in that topic.

* USER STORY [#41](https://github.com/kpetrauskas92/XPLORER/issues/41)

    Post Edit
  * As a user, I want to edit my previously created post so that I can correct mistakes or update its content.

### **5. Like Posts & Comments**

* USER STORY [#43](https://github.com/kpetrauskas92/XPLORER/issues/43)

    Like a Post
  * As a user, I want to like a post so that I can show appreciation for content I enjoy.

* USER STORY [#44](https://github.com/kpetrauskas92/XPLORER/issues/44)

    Like a Comment
  * As a user, I want to like a comment so that I can acknowledge or show agreement with it.

* USER STORY [#45](https://github.com/kpetrauskas92/XPLORER/issues/45)

    View Liked Content
  * As a user, I want to view posts and comments I've previously liked so that I can revisit content that I enjoyed or found valuable.

### **6. Comment Reply**

* USER STORY [#56](https://github.com/kpetrauskas92/XPLORER/issues/56)

    Reply to a Comment
  * As a user, I want to reply directly to another user's comment so that I can interact in a threaded conversation and clarify or discuss specific points.

* USER STORY [#57](https://github.com/kpetrauskas92/XPLORER/issues/57)

    View Threaded Replies
  * As a user, I want to see replies in a threaded format under the original comment so that I can easily follow conversations and understand the context of each reply.

### **7. News Feed**

* USER STORY [#46](https://github.com/kpetrauskas92/XPLORER/issues/46)

    View News Feed
  * As a user, I want to view a news feed so that I can see the latest posts and updates from people I follow and topics I'm interested in.

* USER STORY [#47](https://github.com/kpetrauskas92/XPLORER/issues/47)

    Interact with Feed Items
  * As a user, I want to interact with items on my news feed so that I can like, comment, or share them.

* USER STORY [#48](https://github.com/kpetrauskas92/XPLORER/issues/48)

    Customize News Feed
  * As a user, I want to customize my news feed so that I can choose the type of content I want to see more or less of.

### **8. User Follow/Unfollow**

* USER STORY [#49](https://github.com/kpetrauskas92/XPLORER/issues/49)

    Follow a User
  * As a user, I want to follow another user so that I can see their posts and updates in my news feed.

* USER STORY [#50](https://github.com/kpetrauskas92/XPLORER/issues/50)

    Unfollow a User
  * As a user, I want to unfollow a user so that I no longer see their content in my news feed.

* USER STORY [#51](https://github.com/kpetrauskas92/XPLORER/issues/51)

    View Followers and Following Lists
  * As a user, I want to view lists of users who follow me and users I am following so that I can manage and understand my network on the platform.

### **9. User Search**

* USER STORY [#52](https://github.com/kpetrauskas92/XPLORER/issues/52)

    Basic User Search
  * As a user, I want to search for other users by their username or name so that I can easily find and interact with their profiles.

* USER STORY [#53](https://github.com/kpetrauskas92/XPLORER/issues/53)

    Advanced User Search
  * As a user, I want to filter my search results so that I can narrow down and find specific users based on criteria like location, interests, or mutual connections.

### **10. User Logout**

* USER STORY [#54](https://github.com/kpetrauskas92/XPLORER/issues/54)

    Secure Logout
  * As a logged-in user, I want to log out of my account so that I can ensure my account's security, especially on shared or public devices.

### The Scope Plane

**Features planned:**

* User Registration
  * Users can seamlessly register to the platform, with username, password creation, and feedback mechanisms.
* User Login
  * Existing users can securely log in to their accounts and and view contens of the website.
* User Profile
  * Users can create, view, and edit their profiles. They can also add personal details, pictures, and view their activity.
* Post Creation
  * Users can create, view, edit, and delete their posts. Attachments like images are supported.
* Like Posts & Comments
  * Users can like and unlike posts and comments.
* Comment Reply
  * Users can reply to comments, engage in threaded discussions, and manage (delete) their replies.
* News Feed
  * Users receive a personalized content feed, based on their followed users.
* User Follow/Unfollow
  * Users can follow or unfollow other users, curating their network and content feed.
* User Search
  * An efficient search feature to find users and content.
* Logout
  * Users can securely log out of their accounts.
* Responsive Design
  * The platform is fully responsive to ensure optimal user experience across all device types.

### The Structure Plane

### 1. User Registration

* USER STORY [#26](https://github.com/kpetrauskas92/XPLORER/issues/26)

> Basic Registration - As a new user, I want to register for an account so that I can access the platform's features.

**Acceptance Criteria**:

* Given that I am a new user, When I navigate to the registration page, Then I can provide my details and sign up for an account.

**Implementation**:

* Design a user-friendly registration page.
* Include fields for username, email, password, and any other relevant details.
* Implement backend functionality to securely store user data and complete the registration process.

---

* USER STORY [#28](https://github.com/kpetrauskas92/XPLORER/issues/28)

> Verification - As a registered user, I want my profile to be verified so that other users can trust the authenticity of my profile.

**Acceptance Criteria**:

* Given that I have registered, When I check my email, Then I receive a verification link to confirm my account.

**Implementation**:

* Send a verification email to the user upon registration.
* Incorporate a verification link in the email that, when clicked, confirms the user's email and account.

---

USER STORY [#29](https://github.com/kpetrauskas92/XPLORER/issues/29)
> Social Media Integration - As a user, I want to register on the platform using my social media accounts so that I can simplify the sign-up process and quickly join the community.

**Acceptance Criteria**:

* Given that I am on the registration page, When I choose to sign up with a social media account, Then I can register using my existing social media credentials.

**Implementation**:

* Integrate popular social media platforms (e.g., Facebook, Google, Twitter) for registration.
* Use OAuth or similar protocols for secure social media integration.

---

### 2. User Login

* USER STORY [#30](https://github.com/kpetrauskas92/XPLORER/issues/30)

> Standard Login - As a registered user, I want to log in using my username/email and password so that I can securely access my account.

**Acceptance Criteria**:

* Given that I am a registered user, When I navigate to the login page, Then I can provide my username/email and password to access my account.

**Implementation**:

* Design a user-friendly login page.
* Implement backend functionality to authenticate user credentials and grant access.

---

* USER STORY [#31](https://github.com/kpetrauskas92/XPLORER/issues/31)

> Forgotten Password - As a user who has forgotten my password, I want to reset it so that I can regain access to my account.

**Acceptance Criteria**:

* Given that I am on the login page, When I click on "Forgot Password", Then I can provide my email and receive a link to reset my password.

**Implementation**:

* Incorporate a "Forgot Password" option on the login page.
* Send a password reset link to the user's email upon request.

---

* USER STORY [#32](https://github.com/kpetrauskas92/XPLORER/issues/32)

> Remember Me Option - As a user logging in, I want the platform to remember my session so that I don't have to log in every time I visit.

**Acceptance Criteria**:

* Given that I am logging in, When I select the "Remember Me" option and complete the login, Then my session is remembered, and I don't need to log in again for a specified period.

**Implementation**:

* Incorporate a "Remember Me" checkbox on the login page.
* Use cookies or local storage to remember user sessions for a specified period.

---

### 3. User Profile

* USER STORY [#33](https://github.com/kpetrauskas92/XPLORER/issues/33)

> Viewing Profile - As a registered user, I want to view my profile so that I can see my details and activities.

**Acceptance Criteria**:

* Given that I am logged in, When I navigate to my profile, Then I can see my details, posts, and other activities.

**Implementation**:

* Design a user profile page that displays user details and activities.
* Ensure that the user can easily navigate and interact with their profile elements.

---

* USER STORY [#34](https://github.com/kpetrauskas92/XPLORER/issues/34)

> Editing Profile Details - As a registered user, I want to edit my profile information so that I can keep my details up-to-date.

**Acceptance Criteria**:

* Given that I am on my profile, When I click on "Edit Profile", Then I can update my details and save changes.

**Implementation**:

* Incorporate an "Edit Profile" option on the user's profile page.
* Display the user's current details in an editable form and allow updates.

---

* USER STORY [#35](https://github.com/kpetrauskas92/XPLORER/issues/35)

> Changing Profile Picture - As a registered user, I want to change my profile picture so that I can personalize my profile.

**Acceptance Criteria**:

* Given that I am on my profile, When I click on my profile picture or an "Update Picture" option, Then I can upload a new picture and set it as my profile image.

**Implementation**:

* Provide an option to update the profile picture directly on the profile page.
* Implement backend functionality to securely store and display the new profile picture.

---

* USER STORY [#36](https://github.com/kpetrauskas92/XPLORER/issues/36)

> Setting Profile Preferences - As a registered user, I want to set preferences in my profile so that I can customize my experience on the platform.

**Acceptance Criteria**:

* Given that I am on my profile, When I navigate to settings or preferences, Then I can adjust my profile and platform preferences.

**Implementation**:

* Design a settings or preferences section accessible from the user profile.
* Allow users to customize various aspects of their profile and platform experience.

---

* USER STORY [#40](https://github.com/kpetrauskas92/XPLORER/issues/40)

> Profile Deletion - As a registered user, I want to delete my profile so that my data and activities are permanently removed from the platform.

**Acceptance Criteria**:

* Given that I am on my profile or settings, When I choose to delete my profile and confirm, Then my profile and all associated data are permanently deleted.

**Implementation**:

* Incorporate a "Delete Profile" option in settings or the user profile.
* Ensure secure and permanent deletion of user data upon confirmation.

---

### 4. Post Creation

* USER STORY [#37](https://github.com/kpetrauskas92/XPLORER/issues/37)

> Basic Post Creation - As a user, I want to create a post so that I can share content with others on the platform.

**Acceptance Criteria**:

* Given that I am logged in, When I navigate to a "Create Post" section, Then I can type and publish my content.

**Implementation**:

* Design a user-friendly "Create Post" section or page.
* Implement backend functionality to store and display new posts.

---

* USER STORY [#38](https://github.com/kpetrauskas92/XPLORER/issues/38)

> Adding Images to Post - As a user, I want to add images to my post so that my content can be more engaging and descriptive.

**Acceptance Criteria**:

* Given that I am creating or editing a post, When I choose to add images, Then I can upload and incorporate them into my post.

**Implementation**:

* Incorporate an image upload option in the post creation/edit section.
* Ensure that images are securely stored and displayed within posts.

---

* USER STORY [#39](https://github.com/kpetrauskas92/XPLORER/issues/39)

> Tagging in Posts - As a user, I want to add tags to my post so that it can be more discoverable to users interested in that topic.

**Acceptance Criteria**:

* Given that I am creating or editing a post, When I add tags to my post, Then these tags are associated with my post and can be used for searching or categorizing.

**Implementation**:

* Incorporate a tagging option in the post creation/edit section.
* Store and display tags associated with each post.

---

* USER STORY [#41](https://github.com/kpetrauskas92/XPLORER/issues/41)

> Post Edit - As a user, I want to edit my previously created post so that I can correct mistakes or update its content.

**Acceptance Criteria**:

* Given that I am viewing my post, When I choose to edit it, Then I can modify its content and save the changes.

**Implementation**:

* Provide an "Edit Post" option for each user's posts.
* Display the current post content in an editable format and allow updates.

---

### 5. Like Posts & Comments

* USER STORY [#43](https://github.com/kpetrauskas92/XPLORER/issues/43)

> Like a Post - As a user, I want to like a post so that I can show appreciation for content I enjoy.

**Acceptance Criteria**:

* Given that I am viewing a post, When I click on the "Like" button, Then the post is liked, and the like count increases.

**Implementation**:

* Incorporate a "Like" button for each post.
* Update the like count and store user likes in the backend.

---

* USER STORY [#44](https://github.com/kpetrauskas92/XPLORER/issues/44)

> Like a Comment - As a user, I want to like a comment so that I can acknowledge or show agreement with it.

**Acceptance Criteria**:

* Given that I am viewing a comment, When I click on the "Like" button for that comment, Then the comment is liked, and the like count increases.

**Implementation**:

* Incorporate a "Like" button for each comment.
* Update the like count and store user likes for comments in the backend.

---

* USER STORY [#45](https://github.com/kpetrauskas92/XPLORER/issues/45)

> View Liked Content - As a user, I want to view posts and comments I've previously liked so that I can revisit content that I enjoyed or found valuable.

**Acceptance Criteria**:

* Given that I am on my profile or a designated section, When I navigate to "Liked Content", Then I can see all the posts and comments I have liked.

**Implementation**:

* Design a "Liked Content" section or page accessible from the user profile.
* Display all posts and comments that the user has liked.

---

### 6. Comment Reply

* USER STORY [#56](https://github.com/kpetrauskas92/XPLORER/issues/56)

> Reply to a Comment - As a user, I want to reply directly to another user's comment so that I can interact in a threaded conversation and clarify or discuss specific points.

**Acceptance Criteria**:

* Given that I am viewing a comment, When I choose to reply to it, Then I can type and publish my reply, and it appears as a threaded response below the original comment.

**Implementation**:

* Incorporate a "Reply" option for each comment.
* Display replies in a threaded format below the original comment.

---

* USER STORY [#57](https://github.com/kpetrauskas92/XPLORER/issues/57)

> View Threaded Replies - As a user, I want to see replies in a threaded format under the original comment so that I can easily follow conversations and understand the context of each reply.

**Acceptance Criteria**:

* Given that I am viewing a comment with replies, When I look at the comment section, Then replies appear in a threaded format below the original comment.

**Implementation**:

* Design the comment section to display replies in a threaded format.
* Ensure that the user can easily navigate and interact with comment threads.

---

### 7. News Feed

* USER STORY [#46](https://github.com/kpetrauskas92/XPLORER/issues/46)

> View News Feed - As a user, I want to view a news feed so that I can see the latest posts and updates from people I follow and topics I'm interested in.

**Acceptance Criteria**:

* Given that I am logged in, When I navigate to the main page or news feed, Then I can see the latest posts and updates tailored to my interests.

**Implementation**:

* Design a dynamic news feed that displays content based on user interests and follows.
* Incorporate algorithms or filters to tailor content to individual users.

---

* USER STORY [#47](https://github.com/kpetrauskas92/XPLORER/issues/47)

> Interact with Feed Items - As a user, I want to interact with items on my news feed so that I can like, comment, or share them.

**Acceptance Criteria**:

* Given that I am viewing an item on my news feed, When I choose to like, comment, or share, Then my actions are reflected, and I can interact with the content.

**Implementation**:

* Incorporate interactive elements (like buttons, comment boxes, share options) on each feed item.
* Implement backend functionality to store and reflect user interactions.

---

* USER STORY [#48](https://github.com/kpetrauskas92/XPLORER/issues/48)

> Customize News Feed - As a user, I want to customize my news feed so that I can choose the type of content I want to see more or less of.

**Acceptance Criteria**:

* Given that I am on my news feed or settings, When I adjust my feed preferences, Then my news feed reflects my content preferences.

**Implementation**:

* Design a feed preferences section or option where users can customize their feed content.
* Adjust the news feed display based on user preferences.

---

### 8. User Follow/Unfollow

* USER STORY [#49](https://github.com/kpetrauskas92/XPLORER/issues/49)

> Follow a User - As a user, I want to follow another user so that I can see their posts and updates in my news feed.

**Acceptance Criteria**:

* Given that I am viewing another user's profile, When I click on the "Follow" button, Then I start following that user, and their content appears in my news feed.

**Implementation**:

* Incorporate a "Follow" button on each user's profile.
* Update the follower count and store follow data in the backend.

---

* USER STORY [#50](https://github.com/kpetrauskas92/XPLORER/issues/50)

> Unfollow a User - As a user, I want to unfollow a user so that I no longer see their content in my news feed.

**Acceptance Criteria**:

* Given that I am viewing a profile of a user I follow, When I click on the "Unfollow" button, Then I stop following that user, and their content is removed from my news feed.

**Implementation**:

* Incorporate an "Unfollow" button on profiles of users being followed.
* Update the follower count and adjust the news feed content for the unfollower.

---

USER STORY [#51](https://github.com/kpetrauskas92/XPLORER/issues/51)
> View Followers and Following Lists - As a user, I want to view lists of users who follow me and users I am following so that I can manage and understand my network on the platform.

**Acceptance Criteria**:

* Given that I am on my profile, When I navigate to "Followers" or "Following", Then I can see lists of users who follow me and users I follow.

**Implementation**:

* Design sections or pages to display "Followers" and "Following" lists.
* Display user profiles or names in each list with options to view profiles or unfollow.

---

### 9. User Search

* USER STORY [#52](https://github.com/kpetrauskas92/XPLORER/issues/52)

> Basic User Search - As a user, I want to search for other users by their username or name so that I can easily find and interact with their profiles.

**Acceptance Criteria**:

* Given that I want to find a user, When I use the platform's search function, Then I can enter a username or name and see relevant search results.

**Implementation**:

* Incorporate a search bar or section on the platform.
* Implement backend search functionality to fetch and display relevant user profiles based on search queries.

---

* USER STORY [#53](https://github.com/kpetrauskas92/XPLORER/issues/53)

> Advanced User Search - As a user, I want to filter my search results so that I can narrow down and find specific users based on criteria like location, interests, or mutual connections.

**Acceptance Criteria**:

* Given that I've searched for users, When I apply filters or criteria, Then my search results are refined based on the selected filters.

**Implementation**:

* Incorporate filtering options in the user search section.
* Implement backend functionality to refine search results based on selected criteria.

---

### 10. User Logout

* USER STORY [#54](https://github.com/kpetrauskas92/XPLORER/issues/54)

> Secure Logout - As a logged-in user, I want to log out of my account so that I can ensure my account's security, especially on shared or public devices.

**Acceptance Criteria**:

* Given that I am logged in, When I select the "Logout" option, Then I am securely logged out of my account.

**Implementation**:

* Incorporate a "Logout" button or option on the platform.
* Implement backend functionality to securely end user sessions upon logout.

### The Skeleton Plane

#### Wireframe mock-ups

![Home Page Wireframe]()

#### Database Schema

![Database Schema Diagram]()

### The Surface Plane

#### Design

##### Typography

##### Images

## Features

#### Home page

![Home Page]()

#### Navigation Bar

![Logged in User Nav Bar]()

etc.

## Future Enhancements

## Testing

#### Validator Testing

#### Notable Bugs

#### Technologies Used

#### Packages Used

#### Resources Used

## Deployment

The site was deployed via Heroku, and the live link can be found here - [XPLORER](https://xplorer-p4-ad2c5b0b95ce.herokuapp.com)

### Project Deployment

To deploy the project through Heroku I followed these steps:

* Sign up / Log in to [Heroku](https://www.heroku.com/)
* From the main Heroku Dashboard page select 'New' and then 'Create New App'
* Give the project a name - I entered The-Pantry and select a suitable region, then select create app. The name for the app must be unique.
* This will create the app within Heroku and bring you to the deploy tab. From the submenu at the top, navigate to the resources tab.
* Add the database to the app, in the add-ons section search for 'Heroku Postgres', select the package that appears and add 'Heroku Postgres' as the database
* Navigate to the setting tab, within the config vars section copy the DATABASE_URL to the clipboard for use in the Django configuration.
* Within the django app repository create a new file called env.py - within this file import the os library and set the environment variable for the DATABASE_URL pasting in the address copied from Heroku. The line should appear as os.environ["DATABASE_URL"]= "Paste the link in here"
* Add a secret key to the app using os.environ["SECRET_KEY"] = "your secret key goes here"
* Add the secret key just created to the Heroku Config Vars as SECRET_KEY for the KEY value and the secret key value you created as the VALUE
* In the settings.py file within the django app, import Path from pathlib, import os and import dj_database_url
* insert the line if os.path.isfile("env.py"): import env
* remove the insecure secret key that django has in the settings file by default and replace it with SECRET_KEY = os.environ.get('SECRET_KEY')
* replace the databases section with DATABASES = { 'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))} ensure the correct indentation for python is used.
* In the terminal migrate the models over to the new database connection
* Navigate in a browser to cloudinary, log in, or create an account and log in.
* From the dashboard - copy the CLOUDINARY_URL to the clipboard
* in the env.py file created earlier - add os.environ["CLOUDINARY_URL"] = "paste in the Url copied to the clipboard here"
* In Heroku, add the CLOUDINARY_URL and value copied to the clipboard to the config vars
* Also add the KEY - DISABLE_COLLECTSTATIC with the Value - 1 to the config vars
* this key value pair must be removed prior to final deployment
* Add the cloudinary libraries to the list of installed apps, the order they are inserted is important, 'cloudinary_storage' goes above 'django.contrib.staitcfiles' and 'cloudinary' goes below it.
* in the Settings.py file - add the STATIC files settings - the url, storage path, directory path, root path, media url and default file storage path.
* Link the file to the templates directory in Heroku TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
* Change the templates directory to TEMPLATES_DIR - 'DIRS': [TEMPLATES_DIR]
* Add Heroku to the ALLOWED_HOSTS list the format will be the app name given in Heroku when creating the app followed by .herokuapp.com
* In your code editor, create three new top level folders, media, static, templates
* Create a new file on the top level directory - Procfile
* Within the Procfile add the code - web: guincorn PROJECT_NAME.wsgi
* In the terminal, add the changed files, commit and push to GitHub
* In Heroku, navigate to the deployment tab and deploy the branch manually - watch the build logs for any errors.
* Heroku will now build the app for you. Once it has completed the build process you will see a 'Your App Was Successfully Deployed' message and a link to the app to visit the live site.

#### Forking the repository

By forking the GitHub Repository you can make a copy of the original repository to view or change without it effecting the original repository
This can be done by
    *Log into GitHub or create an account.
    * Locate the repository at <https://github.com/kpetrauskas92/XPLORER> .
    *At the top of the repository, on the right side of the page, select "Fork" from the buttons available.
    * A copy of the repository should now be created in your own repository.

#### Create a clone of this repository

Creating a clone enables you to make a copy of the repository at that point in time - this lets you run a copy of the project locally:
This can be done by:

* Navigate to <https://github.com/kpetrauskas92/XPLORER>
* click on the arrow on the green code button at the top of the list of files
* select the clone by https option and copy the URL it provides to the clipboard
* navigate to your code editor of choice and within the terminal change the directory to the location you want to clone the repository to.
* type 'git clone' and paste the https link you copied from github
* press enter and git will clone the repository to your local machine

### Acknowledgements

I'd like to thank the following:
