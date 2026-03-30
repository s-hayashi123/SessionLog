<script setup lang="ts">
const route = useRoute()
const config = useRuntimeConfig()
const base = config.public.apiBase

const form = reactive({ exercise_id: "", sets: 0, reps: 0, weight: 0 })

const createDetail = async () => {
    await $fetch(`${base}/members/${route.params.id}/sessions/${route.params.session_date}/details`, {
        method: "POST",
        body: form
    })
    await refreshNuxtData()
}

const { data: details } = await useFetch<any[]>(`${base}/members/${route.params.id}/sessions/${route.params.session_date}/details`)
</script>

<template>
    <div>
        <h2>{{ route.params.session_date }}</h2>
        <h3>明細登録</h3>
        <form @submit.prevent="createDetail">
            <input v-model="form.exercise_id" placeholder="種目" required />
            <input v-model="form.sets" placeholder="セット数" type="number" required />
            <input v-model="form.reps" placeholder="レップ数" type="number" required />
            <input v-model="form.weight" placeholder="重量" type="number" step="0.25" required />
            <button type="submit">登録</button>
        </form>
        <h3>セッション内容</h3>
        <ul>
            <li v-for="detail in details" :key="detail.exercise_id"> {{ detail.exercise_id }} / {{ detail.sets }}セット /
                {{ detail.reps }}レップ / {{ detail.weight }}kg </li>
        </ul>
    </div>
</template>