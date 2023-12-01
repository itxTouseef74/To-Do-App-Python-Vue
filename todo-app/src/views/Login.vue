<template>
  <v-container fill-height justify="center" align="center">
    <v-row justify="center" align="center">
      <v-col class="text-h4"> TODO APP </v-col>
    </v-row>
  </v-container>

  <v-container  class="mt-5">
    <v-row justify="center" align="center" >
      <v-col md="6" justify="center" align="center" >
        <v-card class="bg-green-accent-1">
          <v-card-title class="text-h6">
            <b>{{ isLogin ? "Login" : "Signup" }}</b>
          </v-card-title>
          <v-card-text>
            <v-form @submit.prevent="isLogin ? login() : signup()">
              <v-text-field v-model="username" label="Username" required></v-text-field>

              <v-text-field
                v-if="!isLogin"
                v-model="email"
                label="Email"
                required
              ></v-text-field>
              <v-text-field
                v-model="password"
                label="Password"
                type="password"
                required
              ></v-text-field>

              <v-text-field
                v-if="!isLogin"
                v-model="confirm_password"
                label="Confirm Password"
                type="password"
                required
              ></v-text-field>

              <v-btn type="submit" color="primary" class="mr-1">{{
                isLogin ? "Login" : "Signup"
              }}</v-btn>

              <v-btn @click="toggleMode" color="secondary" >
                {{ isLogin ? "Switch to Signup" : "Switch to Login" }}
              </v-btn>
            </v-form>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "Auth",
  data() {
    return {
      isLogin: true,
      username: "",
      email: "",
      password: "",
      confirm_password: "",
    };
  },
  methods: {
    
    login() {
    
      console.log("Login");
      console.log(this.username);
      console.log(this.password);
      if (!this.username || !this.password) {
      console.error("Please enter both username and password.");
      return}
      
      const requestOptions = {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ username: this.username, password: this.password }),
      };

      fetch(`${import.meta.env.VITE_API_BASE_URL}/api/token/`, requestOptions)
        .then((response) => response.json())
        .then((data) => {
          console.log(data.access);
          localStorage.setItem("token", data.access);

          this.$router.push("/");
        })
        .catch((error) => {
          console.error("Error:", error);
        });
    },
    signup() {
      console.log("Signup");
      console.log(this.username);
      console.log(this.email);
      console.log(this.password);
      console.log(this.confirm_password);

      if (this.password !== this.confirm_password) {
        console.error("Passwords do not match.");
        return;
      }

      const requestOptions = {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          username: this.username,
          email: this.email,
          password: this.password,
          confirm_password: this.confirm_password,
        }),
      };

      fetch(`${import.meta.env.VITE_API_BASE_URL}/api/signup/`, requestOptions)
        .then((response) => response.json())
        .then((data) => {
          console.log("Signup successful:", data);
          this.isLogin = true;
        })
        .catch((error) => {
          console.error("Error:", error);
        });
        
    },
    toggleMode() {
      this.isLogin = !this.isLogin;
      this.username = "";
      this.email = "";
      this.password = "";
      this.confirm_password = "";
    },
  },
};
</script>

<style >
body{
  background-color: rgb(239, 243, 246);
}
</style>
