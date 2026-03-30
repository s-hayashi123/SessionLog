<script setup lang="ts">
const config = useRuntimeConfig()
const base = config.public.apiBase

const { data: members } = await useFetch<any[]>(`${base}/members`)
const form = reactive({ name: "", age: "", gender: "", height: "", weight: "", body_fat: "", joined_at: "", memo: "" })

const createMember = async () => {
    await $fetch(`${base}/members`, {
        method: "POST",
        body: form
    })
    await refreshNuxtData()
}
</script>
<template>
    <div>
        <h2>会員の登録</h2>
        <form @submit.prevent="createMember">
            <input v-model="form.name" placeholder="名前" required />
            <input v-model="form.age" placeholder="年齢" type="number" required />
            <select v-model="form.gender" required>
                <option value="">性別を選択</option>
                <option value="男性">男性</option>
                <option value="女性">女性</option>
                <option value="その他">その他</option>
            </select>
            <input v-model="form.height" placeholder="身長(cm)" type="number" step="0.1" required />
            <input v-model="form.weight" placeholder="体重(kg)" type="number" step="0.1" required />
            <input v-model="form.body_fat" placeholder="体脂肪率(%)" type="number" step="0.1" required />
            <input v-model="form.joined_at" type="date" required />
            <input v-model="form.memo" placeholder="メモ" />
            <button type="submit">登録</button>
        </form>
        <h2>会員一覧</h2>
        <ul>
            <li v-for="member in members" :key="member.member_id">
                <NuxtLink :to="`/members/${member.member_id}`">{{ member.name }}</NuxtLink>
            </li>
        </ul>
    </div>
</template>
