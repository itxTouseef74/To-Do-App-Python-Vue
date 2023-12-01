# Todo App

This Todo App is a full-stack application that combines the power of Vue.js and Vuetify on the frontend with Django and Django Rest Framework on the backend. Users can securely manage their tasks with features like task creation, updating, and deletion, all within an authenticated environment.

## Features

- **User Authentication**: Secure user signup and login functionalities.
- **Todo Management**: Add, update, and delete tasks with fields for title, description, date, and completion status.
- **Fully Functional**: A fully functional todo application with the ability to perform CRUD operations on tasks.
- **Vue.js and Vuetify**: A modern and responsive frontend built with Vue.js and Vuetify.
- **Django and Django Rest Framework**: A robust and secure backend using Django and Django Rest Framework.

## Requirements

- Node.js for frontend development.
- Python and Django for the backend.
- Vue.js and Vuetify for the frontend.

## Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/itxTouseef74/To-Do-App-Python-Vue.git
   ```

2. **Backend Setup:**

   - Navigate to the backend directory:

     ```bash
     cd Todo
     ```

   - Create and apply migrations:

     ```bash
     python manage.py makemigrations
     python manage.py migrate
     ```

   - Start the Django development server:

     ```bash
     python manage.py runserver
     ```

3. **Frontend Setup:**

   - Navigate to the frontend directory:

     ```bash
     cd todo-app
     ```

   - Install dependencies:

     ```bash
     npm install
     ```

   - Start the Vue.js development server:

     ```bash
     npm run dev
     ```

4. **Access the App:**

   - Open your web browser and navigate to `http://localhost:5137` to use the Todo App.

## Usage

1. **User Authentication:**
   - Sign up for a new account or log in if you already have one.

![image](https://github.com/itxTouseef74/To-Do-App-Python-Vue/assets/116633040/74d0a695-bcb1-4187-befb-2775b4678257)

![image](https://github.com/itxTouseef74/To-Do-App-Python-Vue/assets/116633040/dde3bf09-e3bf-4085-a55d-d178dadf536a)



3. **Todo Management:**
   - Add new tasks with title, description, date, and completion status.
   - Update tasks with the latest information.
   - Delete tasks that are no longer needed.


![image](https://github.com/itxTouseef74/To-Do-App-Python-Vue/assets/116633040/16cdf11e-abf7-4ff0-bd60-0f8f8acaa80a)

![image](https://github.com/itxTouseef74/To-Do-App-Python-Vue/assets/116633040/dea17505-f80c-4a2c-9b21-66dd5e792205)


## Contributing

Contributions are welcome! If you want to contribute to this project, follow these steps:

1. Fork this repository.
2. Create a new branch: `git checkout -b feature/your-feature`.
3. Make your changes and commit them: `git commit -m "Add your feature"`.
4. Push to the branch: `git push origin feature/your-feature`.
5. Create a pull request explaining your changes.


## Acknowledgments

- This project was developed to provide a comprehensive Todo App using Vue.js, Vuetify, Django, and Django Rest Framework.
