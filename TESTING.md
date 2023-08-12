# Manual Testing

In the process of ensuring the functionality and user experience of the platform, manual testing was conducted on various aspects of the application. The manual testing focused on validating the features outlined in the provided user stories, which define the core functionalities of the platform. Each user story represents a specific user requirement, and the associated acceptance criteria guide the expected behavior of the platform.

The following sections provide a comprehensive overview of the manual testing steps undertaken for each user story, along with the observed results. These tests aim to verify that the platform functions as intended and meets the expectations set by the user stories. While these tests provide an initial assessment of the platform's functionality, it's important to note that comprehensive testing includes various scenarios and edge cases that may not be covered within this scope.

## 1. User Registration

### a. Basic Registration

**Test Case:** Register as a new user using the platform's registration form.

**Steps:**

- Navigate to the registration page.
- Fill in the required fields: username, email, password, and other relevant details.
- Submit the form.

**Expected Result:** A new account should be created, and the user should be directed to a confirmation or welcome page.

**Actual Result:** Account successfully created and user directed to a welcome page.

**Status:** Pass

## 2. User Login

### a. Standard Login

**Test Case:** Log in using username/email and password.

**Steps:**

- Navigate to the login page.
- Enter valid username/email and password.
- Click on the "Login" button.

**Expected Result:** The user should be authenticated and directed to the platform's main page.

**Actual Result:** User successfully logged in and redirected to the main page.

**Status:** Pass

### c. Remember Me Option

**Test Case:** Log in with the "Remember Me" option.

**Steps:**

- Enter valid username/email and password.
- Check the "Remember Me" checkbox.
- Click on the "Login" button.

**Expected Result:** The user's session should be remembered, and they should stay logged in even after closing the browser or navigating away.

**Actual Result:** Session successfully remembered; user remains logged in.

**Status:** Pass

## 3. User Profile

### a. Viewing Profile

**Test Case:** View user profile details and activities.

**Steps:**

- Log in with a registered account.
- Navigate to the user's profile page.

**Expected Result:** The user's details, posts, and activities should be displayed on the profile page.

**Actual Result:** User profile successfully displayed with all relevant details.

**Status:** Pass

### b. Editing Profile Details

**Test Case:** Edit user profile information.

**Steps:**

- Log in with a registered account.
- Navigate to the user's profile page.
- Click on the "Edit Profile" button.
- Update some profile details (e.g., bio, location).
- Save the changes.

**Expected Result:** The profile details should be updated with the new information.

**Actual Result:** Profile details successfully updated with the new information.

**Status:** Pass

### c. Changing Profile Picture

**Test Case:** Change user profile picture.

**Steps:**

- Log in with a registered account.
- Navigate to the user's profile page.
- Click on the profile picture or "Update Picture" option.
- Upload a new picture.
- Save the changes.

**Expected Result:** The profile picture should be updated with the newly uploaded image.

**Actual Result:** Profile picture successfully changed to the new image.

**Status:** Pass

### d. Setting Profile Preferences

**Test Case:** Set user profile preferences.

**Steps:**

- Log in with a registered account.
- Navigate to the user's profile page.
- Access the "Edit" or "Preferences" section.
- Customize profile and platform preferences (e.g., profile image).
- Save the changes.

**Expected Result:** The selected profile preferences should be saved and applied.

**Actual Result:** Profile preferences successfully set and applied.

**Status:** Pass

## 4. Post Creation

### a. Basic Post Creation

**Test Case:** Create a new post on the platform.

**Steps:**

- Log in with a registered account.
- Navigate to the "Create Post" section/page.
- Enter the post content.
- Click on the "Publish" or "Post" button.

**Expected Result:** The new post should be successfully created and displayed on the platform.

**Actual Result:** New post successfully created and displayed.

**Status:** Pass

### b. Adding Images to Post

**Test Case:** Add images to a post.

**Steps:**

- Log in with a registered account.
- Create a new post.
- Use the "Browse" option to upload and attach an image.
- Save or update the post.

**Expected Result:** The image should be added to the post and displayed along with the content.

**Actual Result:** Image successfully added to the post and displayed.

**Status:** Pass

### d. Post Edit

**Test Case:** Edit a previously created post.

**Steps:**

- Log in with a registered account.
- Navigate to the post that needs editing.
- Click on the "Edit Post" option.
- Modify the post content.
- Save the changes.

**Expected Result:** The post content should be updated with the new information.

**Actual Result:** Post content successfully updated with the new changes.

**Status:** Pass

## 5. Like Posts & Comments

### a. Like a Post

**Test Case:** Like a post on the platform.

**Steps:**

- Log in with a registered account.
- Navigate to a post in the news feed or profile.
- Click on the "Like" button associated with the post.

**Expected Result:** The post should be liked, and the like count should increase by one.

**Actual Result:** Post successfully liked, and like count increased.

**Status:** Pass

### b. Like a Comment

**Test Case:** Like a comment on the platform.

**Steps:**

- Log in with a registered account.
- Navigate to a post with comments.
- Find a comment and click on its "Like" button.

**Expected Result:** The comment should be liked, and the like count should increase by one.

**Actual Result:** Comment successfully liked, and like count increased.

**Status:** Pass

## 6. Comments

### a. Reply to a Comment

**Test Case:** Reply to a comment and create a threaded conversation.

**Steps:**

- Log in with a registered account.
- Navigate to a post with comments.
- Find a comment and click on its "Reply" button.
- Type in the reply and submit it.

**Expected Result:** The reply should be posted below the original comment, creating a threaded conversation.

**Actual Result:** Reply successfully posted as a threaded response.

**Status:** Pass

### b. Delete a Comment

**Test Case:** Delete a previously posted comment.

**Steps:**

- Log in with a registered account.
- Navigate to a post with your own comments.
- Find the comment you wish to delete.
- Click on the "Delete" button associated with the comment.

**Expected Result:** The comment should be deleted and removed from the thread.

**Actual Result:** Comment successfully deleted, and it's removed from the thread.

**Status:** Pass

### c. View Threaded Replies

**Test Case:** View replies in a threaded format under the original comment.

**Steps:**

- Log in with a registered account.
- Navigate to a post with threaded comments.
- Click on a comment to view its threaded replies.

**Expected Result:** Replies should be displayed in a threaded format under the original comment.

**Actual Result:** Threaded replies successfully displayed under the original comment.

**Status:** Pass

## 7. News Feed

### a. View News Feed

**Test Case:** View the user's personalized news feed.

**Steps:**

- Log in with a registered account.
- Navigate to the main page or news feed.

**Expected Result:** The user should see the latest posts and updates from people they follow.

**Actual Result:** News feed successfully displayed with relevant content.

**Status:** Pass

### b. Interact with Feed Items

**Test Case:** Interact with posts in the news feed (like).

**Steps:**

- Log in with a registered account.
- Scroll through the news feed and find a post.
- Like, comment, or share the post.

**Expected Result:** The user's interaction (like) should be reflected on the post.

**Actual Result:** Interaction (like) successfully recorded and displayed.

**Status:** Pass

## 8. User Follow/Unfollow

### a. Follow a User

**Test Case:** Follow another user's profile.

**Steps:**

- Log in with a registered account.
- Navigate to another user's profile page.
- Click on the "Follow" button.

**Expected Result:** The user should start following the selected user, and their content should appear in the news feed.

**Actual Result:** Successfully started following the user, and their content appears in the news feed.

**Status:** Pass

### b. Unfollow a User

**Test Case:** Unfollow a user's profile.

**Steps:**

- Log in with a registered account.
- Navigate to the profile of a user being followed.
- Click on the "Unfollow" button.

**Expected Result:** The user should stop following the selected user, and their content should be removed from the news feed.

**Actual Result:** Successfully stopped following the user, and their content is removed from the news feed.

**Status:** Pass

## 9. User Search

### a. Basic User Search

**Test Case:** Search for other users by their username.

**Steps:**

- Log in with a registered account.
- Navigate to the platform's search bar or section.
- Enter the username of a user to search for.

**Expected Result:** Relevant user profiles should be displayed based on the search query.

**Actual Result:** User profiles matching the search query successfully displayed.

**Status:** Pass

## 10. User Logout

### a. Secure Logout

**Test Case:** Log out of the user account securely.

**Steps:**

- Log in with a registered account.
- Navigate to the user profile or settings.
- Click on the "Logout" option.

**Expected Result:** The user should be securely logged out of the account.

**Actual Result:** User successfully logged out, and session is terminated.

**Status:** Pass

## Compatibility Testing

### Browser Compatibility Testing

**Test Case:** Verify compatibility with various web browsers.

**Steps:**

1. Open the application in Chrome.
2. Navigate through different sections and functionalities.
3. Perform actions such as registration, login, post creation, and interaction.
4. Repeat steps 1-3 in Firefox, Safari, Microsoft Edge, and Internet Explorer.

**Expected Result:** The application should work smoothly and consistently across all tested browsers.

**Actual Result:** The application performs well in Chrome, Firefox, Safari, Microsoft Edge, and Internet Explorer.

**Status:** Pass

### Mobile Device Compatibility Testing

**Test Case:** Verify compatibility with mobile devices.

**Steps:**

1. Open the application on Android smartphones and tablets.
2. Navigate through different sections and functionalities.
3. Perform actions such as registration, login, post creation, and interaction.
4. Repeat steps 1-3 on iOS devices (different iPhone and iPad models).

**Expected Result:** The application should be responsive and user-friendly on various mobile devices.

**Actual Result:** The application's responsiveness and functionality are consistent across Android and iOS devices.

**Status:** Pass

### Screen Size and Resolution Testing

**Test Case:** Verify compatibility with different screen sizes and resolutions.

**Steps:**

1. Open the application on devices with varying screen sizes and resolutions.
2. Navigate through different sections and functionalities.
3. Verify that the user interface elements adjust appropriately to different screen sizes.

**Expected Result:** The application's user interface should adapt to different screen sizes and resolutions.

**Actual Result:** The user interface remains readable and usable across various screen sizes and resolutions.

**Status:** Pass

### Different Device Orientations

**Test Case:** Verify compatibility with different device orientations.

**Steps:**

1. Open the application on mobile devices in both portrait and landscape orientations.
2. Navigate through different sections and functionalities.
3. Verify that the user interface remains usable in both orientations.

**Expected Result:** The user interface should work well in both portrait and landscape orientations.

**Actual Result:** The user interface remains functional and user-friendly in both orientations.

**Status:** Pass

### JavaScript and CSS Compatibility

**Test Case:** Verify compatibility with JavaScript and CSS across different browsers.

**Steps:**

1. Open the application in various browsers.
2. Verify that JavaScript-based interactions work as intended.
3. Ensure CSS styling remains consistent and accurate across browsers.

**Expected Result:** JavaScript functionality and CSS styling should work consistently across all tested browsers.

**Actual Result:** JavaScript interactions and CSS styling are consistent and accurate across different browsers.

**Status:** Pass
