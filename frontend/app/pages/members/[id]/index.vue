<script setup lang="ts">
const route = useRoute()
const config = useRuntimeConfig()
const base = config.public.apiBase

const { data: member } = await useFetch<any>(`${base}/members/${route.params.id}`)
const { data: sessions } = await useFetch<any[]>(`${base}/members/${route.params.id}/sessions`)
const form = reactive({ memo: "" })

const createSession = async () => {
    await $fetch(`${base}/members/${route.params.id}/sessions`, {
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
        <p>入会日: {{ member?.joined_at?.slice(0, 10) }}</p>

        <h3>セッション登録</h3>
        <form @submit.prevent="createSession">
            <input v-model="form.memo" placeholder="メモ" />
            <button type="submit">登録</button>
        </form>

        <h3>セッション一覧</h3>
        <ul>
            <li v-for="session in sessions" :key="session.session_date">
                <NuxtLink :to="`/members/${route.params.id}/sessions/${session.session_date}`">
                    {{ session.session_date }}
                </NuxtLink>
            </li>
        </ul>
    </div>
</template>
