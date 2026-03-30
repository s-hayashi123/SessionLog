<script setup lang="ts">
const { data: members } = await useFetch<any[]>("https://98af1h91g3.execute-api.ap-northeast-1.amazonaws.com/Prod/members")

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