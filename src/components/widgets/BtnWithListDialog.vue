<template>
  <v-dialog :max-width="maxWidth">
    <template v-slot:activator="{ props: activatorProps }">
      <v-btn v-bind="activatorProps" :text="btnText" class="mb-2 mr-2"/>
    </template>
    <template v-slot:default="{ isActive }">
      <v-card :title="headerText">
        <v-card-text>
          <v-data-table-virtual
            height="400"
            item-value="name"
            :width="maxWidth"
            :headers="headers"
            :items="items"
          />
        </v-card-text>
        <v-card-actions>
          <v-spacer/>
          <v-btn text="Закрыть список" @click="isActive.value = false"/>
        </v-card-actions>
      </v-card>
    </template>
  </v-dialog>
</template>

<script>
export default {
  name: 'BtnWithListDialog',
  props: {
    headerText: {type:String, required: true},
    headers: { type: Array, required: true },
    items: { type: Array, required: true },
    btnText: { type: String, required: true },
    maxWidth: { type: Number, required: true},
  }
}
</script>