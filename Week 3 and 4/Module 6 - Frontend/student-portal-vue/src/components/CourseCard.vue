<template>

<div class="card">

    <h2>{{ name }}</h2>

    <p>Code : {{ code }}</p>

    <p>Credits : {{ credits }}</p>

    <p>Grade : {{ grade }}</p>

</div>

</template>

<script setup>

defineProps({

    name:String,

    code:String,

    credits:Number,

    grade:String

})

</script>

<style scoped>

.card{

    background:white;

    padding:20px;

    margin:20px 0;

    border-radius:10px;

    box-shadow:0 2px 8px rgba(0,0,0,.2);

}

</style>