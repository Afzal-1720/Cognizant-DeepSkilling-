<template>

<h2>Course Details</h2>

<p>

Course ID :

{{ id }}

</p>

<button @click="enroll">

Enroll

</button>

</template>

<script setup>

import {

useRoute,

useRouter

}

from 'vue-router'

const route=useRoute()

const router=useRouter()

const id=route.params.id

function enroll(){

router.push('/profile')

}

</script>