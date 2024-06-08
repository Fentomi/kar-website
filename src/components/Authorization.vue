<template>
  <div class="wrapper">
    <h1 class="mb-3">Авторизация</h1>
    <v-text-field
      v-model="userLogin"
      label="Login"
    />
    <v-text-field
      v-model="userPassword"
      label="Password"
    />
    <div v-if="showErrorMessage" class="mb-4">
      Неверный логин или пароль. <br> 
      Пожалуйста, попробуйте еще раз.
    </div>
    <v-btn class="btn" type="submit" block @click="onAuthorizationAttempt"> 
      Авторизоваться 
    </v-btn>
  </div>
</template>

<script>
export default {
  name: 'Authorization',
  props: {
    userIsAuthorized: Boolean,
  },
  data() {
    return {
      userLogin: '',
      userPassword: '',
      showErrorMessage: false,
    }
  },
  methods: {
    onAuthorizationAttempt() {
      let isCurrentUser = false;
      const testData = {
        login: 'admin',
        password: '1111',
      }
      if(this.userLogin === testData.login && this.userPassword === testData.password) isCurrentUser = true;
      return isCurrentUser ? this.$emit('updateUserIsAuthorized', isCurrentUser) : this.showErrorMessage = true;
    }
  },
}
</script>