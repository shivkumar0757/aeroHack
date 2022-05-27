<template>
  <div class="hello">
    <Header />

    <div>
      <Data :data="data" />
      <button @click="getData()">check status</button>
    </div>
  </div>
</template>

<script>
import Header from "./Header.vue";
import Data from "./Data.vue";
import { getData } from "../services/UserService";

export default {
  name: "Dashboard",
  components: {
    Header,
    Data,
  },
  data() {
    return {
      data: "localData",
    };
  },
  methods: {
    getData() {
      getData().then((response) => {
        this.data = response;
      });
    },
  },
  mounted() {
    // this.getData();
  },
};
</script>
