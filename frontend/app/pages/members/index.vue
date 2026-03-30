<script setup lang="ts">
const { data: members } = await useFetch<any[]>("http://localhost:8000/members")

</script>
<template>
    <div>
        <h2>会員一覧</h2>
        <ul>
            <li v-for="member in members" key={{member.member_id}}>
                <NuxtLink :to="`/members/${member.member_id}`">{{ member.name }}</NuxtLink>
            </li>
        </ul>
    </div>
</template>