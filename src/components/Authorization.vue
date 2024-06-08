<template>
  <div class="header">
    <p class="header-text">CA<span style="color: palevioletred;">KE</span></p>
  </div>
  <div class="wrapper">
    <h1 class="mb-3">Сначала авторизуйтесь!</h1>
    <p class="mb-2" style="font-weight: bold;">Логин: *</p>
    <v-text-field
      class="mb-3"
      v-model="userLogin"
      label="example@gmail.com"
    />
    <p class="mb-2" style="font-weight: bold;">Пароль: *</p>
    <v-text-field
      class="mb-3"
      v-model="userPassword"
      label="****"
    />
    <div v-if="showErrorMessage" class="mb-3">Неверный логин или пароль, повторите попытку еще раз</div>
    <v-btn width="120" class="btn" type="submit" @click="onAuthorizationAttempt"> 
      Войти 
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
      let currentRole = 0;
      const menedger = {
        login: 'menedger',
        password: '1111',
        role: 1
      }
      const conditer = {
        login: 'shef',
        password: '1111',
        role: 2
      }
      if(this.userLogin === menedger.login && this.userPassword === menedger.password) {
        isCurrentUser = true;
        currentRole = menedger.role;
      }
      if(this.userLogin === conditer.login && this.userPassword === conditer.password) {
        isCurrentUser = true;
        currentRole = conditer.role;
      }
      this.userLogin = '';
      this.userPassword = '';
      return isCurrentUser ? this.$emit('updateUserIsAuthorized', {isCurrentUser: isCurrentUser, currentRole: currentRole}) : this.showErrorMessage = true;
    }
  },
}
</script>

<style scoped lang="scss">
.header {
  .header-text {
    margin-left: 120px;
    font-size: 52px;
    font-weight: bold;
  }
}
.wrapper {
  margin: 0 auto;
  width: 500px;
  h1 {
    display: block;
    text-align: center;
  }
  .btn {
    display: block;
    margin: 0 auto;
    border-radius: 50px;
    background-color: blueviolet;
    color: white;
  }
}
</style>