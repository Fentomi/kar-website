<template>
  <Authorization
    v-if="!userIsAuthorized"
    :user-is-authorized="userIsAuthorized"
    @updateUserIsAuthorized="onUpdateUserIsAuthorized"
  />
  <Main
    v-if="userIsAuthorized"
    @logout="userIsAuthorized=false"
    :currentRole="currentRole"
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
      userIsAuthorized: true,
      currentRole: 1
    }
  },
  methods: {
    onUpdateUserIsAuthorized(data) {
      this.userIsAuthorized = data['isCurrentUser'];
      this.currentRole = data['currentRole'];
    }
  }
}
</script>

<style>
.v-table__wrapper {
  overflow-x: hidden !important;
}
</style>