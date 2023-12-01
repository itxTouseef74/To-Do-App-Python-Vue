<template>
  <v-container class="mt-1">
    <v-col align="end">
      <v-btn variant="tonal" v-if="isLoggedIn" @click="logout()" color="red" class="mt-1"
        >Logout</v-btn
      ></v-col
    >
    <v-row>
      <v-col md="6" class="mx-auto">
        <v-card class="bg-green-accent-1">
          <v-card-title class="text-h6">
            <b>Create Todo</b>
          </v-card-title>
          <v-card-text>
            <div class="form-group">
              <v-text-field v-model="todo_name" label="Title" required></v-text-field>
              <v-text-field
                v-model="todo_description"
                label="Description"
                required
              ></v-text-field>
              <v-text-field
                v-model="todo_date"
                type="date"
                label="Task Date"
                required
              ></v-text-field>

              <v-select
                v-model="is_completed"
                :items="['Incomplete', 'Completed']"
                label="Status"
                required
              ></v-select>

              <v-btn @click="createTodo" color="success">Create Todo</v-btn>
            </div>
          </v-card-text>
        </v-card>
      </v-col>

      <v-col md="6" class="mx-auto">
        <v-card class="bg-green-accent-1">
          <v-card-title class="text-h6">
            <b>Todo List</b>
          </v-card-title>
          <v-list class="bg-green-accent-1">
            <v-list-item v-for="todo in todos" :key="todo.uuid">
              <v-list-item-content>
                <v-list-item-title>
                  <b>Title:</b> {{ todo.todo_name }}
                </v-list-item-title>
                <v-list-item-subtitle>
                  <b>Description:</b> {{ todo.todo_description }}
                </v-list-item-subtitle>
                <v-list-item-subtitle>
                  <b>Task Date:</b>{{ todo.todo_date }}
                </v-list-item-subtitle>
                <v-list-item-subtitle
                  class="mb-1"
                  :style="{ color: displayStatusColor(todo.is_completed) }"
                  ><b>Status:</b> {{ displayStatus(todo.is_completed) }}
                </v-list-item-subtitle>
              </v-list-item-content>
              <v-list-item-action>
                <v-btn @click="deleteTodo(todo.uuid)" color="red" class="mr-1"
                  >Delete Todo</v-btn
                >
                <v-btn @click="openUpdateDialog(todo)" color="primary">Update</v-btn>
              </v-list-item-action>
            </v-list-item>
          </v-list>
        </v-card>
      </v-col>
    </v-row>
    <v-dialog v-model="showUpdateDialog" max-width="600">
      <v-card>
        <v-card-title class="text-h6">
          <b>Update Todo</b>
        </v-card-title>
        <v-card-text>
          <v-text-field
            v-model="updatedTask.todo_name"
            label="Title"
            required
          ></v-text-field>
          <v-text-field
            v-model="updatedTask.todo_description"
            label="Description"
            required
          ></v-text-field>
          <v-text-field
            v-model="updatedTask.todo_date"
            label="Task Date"
            type="date"
            required
          ></v-text-field>
          <v-select
            v-model="updatedTask.todo"
            :items="['Incomplete', 'Completed']"
            label="Status"
            required
          ></v-select>
        </v-card-text>
        <v-card-actions>
          <v-btn @click="updateTodo" color="primary">Update</v-btn>
          <v-btn @click="closeUpdateDialog" color="red">Cancel</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script>
export default {
  name: "Todo",
  data() {
    return {
      todo_name: "",
      todo_description: "",
      is_completed: "",
      todo_date: "",
      todos: [],
      isLoggedIn: false,
      showUpdateDialog: false,
      updatedTask: {
        uuid: null,
        todo_name: "",
        todo_description: "",
        is_completed: "",
        todo_date: "",
      },
    };
  },
  created() {
    if (localStorage.getItem("token")) {
      this.isLoggedIn = true;
    }
    this.getTodos();
  },
  methods: {
    getTodos() {
      const token = localStorage.getItem("token");
      const requestOptions = {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`,
        },
      };

      fetch(`${import.meta.env.VITE_API_BASE_URL}/api/todo/`, requestOptions)
        .then((response) => response.json())
        .then((data) => {
          this.todos = data.data;
        })
        .catch((error) => {
          console.error("Error fetching todos:", error);
        });
    },
    createTodo() {
      const token = localStorage.getItem("token");
      const requestOptions = {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify({
          todo_name: this.todo_name,
          todo_description: this.todo_description,
          todo_date: this.todo_date,
          is_completed: this.is_completed === "Completed" ? true : false,
        }),
      };

      fetch(`${import.meta.env.VITE_API_BASE_URL}/api/todo/`, requestOptions)
        .then((response) => response.json())
        .then((data) => {
          console.log("Todo created:", data);
          this.getTodos();
        })
        .catch((error) => {
          console.error("Error creating todo:", error);
        });
    },
    deleteTodo(uuid) {
      const token = localStorage.getItem("token");
      const requestOptions = {
        method: "DELETE",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify({ uuid: uuid }),
      };

      fetch(`${import.meta.env.VITE_API_BASE_URL}/api/todo/delete/`, requestOptions)
        .then((response) => response.json())
        .then((data) => {
          console.log(data);
          this.getTodos();
        });
    },
    openUpdateDialog(todo) {
      this.showUpdateDialog = true;
      this.updatedTask = {
        ...todo,
        todo: todo.is_completed ? "Completed" : "Incomplete",
      };
    },
    closeUpdateDialog() {
      this.showUpdateDialog = false;
    },

    updateTodo(uuid, is_completed) {
      const token = localStorage.getItem("token");
      const requestOptions = {
        method: "PATCH",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify({
          uuid: this.updatedTask.uuid,
          todo_name: this.updatedTask.todo_name,
          todo_description: this.updatedTask.todo_description,
          todo_date: this.updatedTask.todo_date,
          is_completed: this.updatedTask.todo === "Completed" ? true : false,
        }),
      };

      fetch(`${import.meta.env.VITE_API_BASE_URL}/api/todo/`, requestOptions)
        .then((response) => response.json())
        .then((data) => {
          console.log(data);
          this.getTodos();
          this.closeUpdateDialog();
        });
    },
    displayStatus(todo) {
      return todo ? "Completed" : "Incomplete";
    },
    displayStatusColor(isCompleted) {
      return isCompleted ? "green" : "red";
    },
    logout() {
      localStorage.removeItem("token");
      window.location.href = "/login";
    },
  },
};
</script>

<style>
body {
  background-color: rgb(239, 243, 246);
}
</style>
