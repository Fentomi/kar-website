<template>
  <Authorization
    v-if="!userIsAuthorized"
    :user-is-authorized="userIsAuthorized"
    @updateUserIsAuthorized="userIsAuthorized=true"
  />
  <Main
    v-if="userIsAuthorized"
    @logout="userIsAuthorized=false"
  />
</template>

<script>
import Authorization from '@/components/Authorization.vue';
import Main from '@/components/Main.vue';

export default {
  name: 'App',
  components: {
    Authorization,
    Main,
  },
  data() {
    return {
      userIsAuthorized: false,
    }
  }
}
</script>

<style>
.wrapper {
  margin: 30vh auto;
  width: 700px;
}
.v-table__wrapper {
  overflow-x: hidden !important;
}
</style>