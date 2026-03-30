<script setup lang="ts">
const route = useRoute()
const { data: member } = await useFetch<any>(`http://localhost:8000/members/${route.params.id}`)
const { data: sessions } = await useFetch<any[]>(`http://localhost:8000/members/${route.params.id}/sessions`)
const form = reactive({ memo: "" })

const createSession = async () => {
    await $fetch(`http://localhost:8000/members/${route.params.id}/sessions`, {
        method: "POST",
        body: form
    })
    refreshNuxtData()
}
</script>

<template>
    <div>
        <h2>{{ member?.name }}</h2>
        <p>年齢: {{ member?.age }}</p>
        <p>入会日: {{ member?.joined_at }}</p>

        <h3>セッション登録</h3>
        <form @submit.prevent="createSession">
            <input v-model="form.memo" placeholder="メモ" />
            <button type="submit">登録</button>
        </form>

        <h3>セッション一覧</h3>
        <ul>
            <li v-for="session in sessions" :key="session.session_date">{{ session.session_date }}</li>
        </ul>
    </div>
</template>