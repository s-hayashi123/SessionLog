<script setup lang="ts">
const config = useRuntimeConfig()
const base = config.public.apiBase

import type { Member } from '../../types'

const { data: members } = await useFetch<Member[]>(`${base}/members`)
const form = reactive({ name: "", age: "", gender: "", height: "", weight: "", body_fat: "", joined_at: "", memo: "" })

const showForm = ref(false)

const createMember = async () => {
    await $fetch(`${base}/members`, {
        method: "POST",
        body: form
    })
    showForm.value = false
    await refreshNuxtData()
}
</script>

<template>
    <div>
        <!-- Header Section -->
        <div class="flex items-center justify-between mb-6">
            <div>
                <h2 class="text-xl font-700 text-text-primary">会員一覧</h2>
                <p class="text-sm text-text-muted mt-0.5">{{ members?.length || 0 }} 名</p>
            </div>
            <button @click="showForm = !showForm"
                class="bg-accent text-surface font-600 text-sm px-4 py-2 rounded-lg hover:bg-accent-hover transition-all cursor-pointer active:scale-95">
                {{ showForm ? '閉じる' : '+ 新規登録' }}
            </button>
        </div>

        <!-- Registration Form -->
        <Transition name="slide">
            <form v-if="showForm" @submit.prevent="createMember"
                class="bg-surface-raised border border-border-subtle rounded-xl p-5 mb-6 space-y-3">
                <p class="text-xs text-text-muted uppercase tracking-widest font-500 mb-1">会員情報</p>

                <input v-model="form.name" placeholder="名前" required
                    class="w-full bg-input-bg border border-input-border rounded-lg px-4 py-2.5 text-text-primary placeholder:text-text-muted focus:outline-none focus:border-input-focus transition-colors" />

                <div class="grid grid-cols-2 gap-3">
                    <input v-model="form.age" placeholder="年齢" type="number" required
                        class="bg-input-bg border border-input-border rounded-lg px-4 py-2.5 text-text-primary placeholder:text-text-muted focus:outline-none focus:border-input-focus transition-colors" />
                    <select v-model="form.gender" required
                        class="bg-input-bg border border-input-border rounded-lg px-4 py-2.5 text-text-primary focus:outline-none focus:border-input-focus transition-colors">
                        <option value="" class="text-text-muted">性別</option>
                        <option value="男性">男性</option>
                        <option value="女性">女性</option>
                        <option value="その他">その他</option>
                    </select>
                </div>

                <div class="grid grid-cols-3 gap-3">
                    <input v-model="form.height" placeholder="身長cm" type="number" step="0.1" required
                        class="bg-input-bg border border-input-border rounded-lg px-4 py-2.5 text-text-primary placeholder:text-text-muted focus:outline-none focus:border-input-focus transition-colors" />
                    <input v-model="form.weight" placeholder="体重kg" type="number" step="0.1" required
                        class="bg-input-bg border border-input-border rounded-lg px-4 py-2.5 text-text-primary placeholder:text-text-muted focus:outline-none focus:border-input-focus transition-colors" />
                    <input v-model="form.body_fat" placeholder="体脂肪%" type="number" step="0.1" required
                        class="bg-input-bg border border-input-border rounded-lg px-4 py-2.5 text-text-primary placeholder:text-text-muted focus:outline-none focus:border-input-focus transition-colors" />
                </div>

                <input v-model="form.joined_at" type="date" required
                    class="w-full bg-input-bg border border-input-border rounded-lg px-4 py-2.5 text-text-primary focus:outline-none focus:border-input-focus transition-colors" />
                <input v-model="form.memo" placeholder="メモ（任意）"
                    class="w-full bg-input-bg border border-input-border rounded-lg px-4 py-2.5 text-text-primary placeholder:text-text-muted focus:outline-none focus:border-input-focus transition-colors" />

                <button type="submit"
                    class="w-full bg-accent text-surface font-600 rounded-lg py-2.5 hover:bg-accent-hover transition-all cursor-pointer active:scale-[0.98] mt-2">
                    登録する
                </button>
            </form>
        </Transition>

        <!-- Member List -->
        <ul class="space-y-2">
            <li v-for="member in members" :key="member.member_id">
                <NuxtLink :to="`/members/${member.member_id}`"
                    class="flex items-center justify-between bg-surface-raised border border-border-subtle rounded-xl px-5 py-4 hover:bg-surface-hover hover:border-accent/30 transition-all group">
                    <div>
                        <p class="font-600 text-text-primary group-hover:text-accent transition-colors">{{ member.name }}</p>
                        <p class="text-xs text-text-muted mt-0.5">{{ member.gender }} · {{ member.age }}歳</p>
                    </div>
                    <span class="text-text-muted group-hover:text-accent transition-colors text-lg">›</span>
                </NuxtLink>
            </li>
        </ul>

        <p v-if="!members?.length" class="text-center text-text-muted py-12 text-sm">
            まだ会員が登録されていません
        </p>
    </div>
</template>

<style scoped>
.slide-enter-active,
.slide-leave-active {
    transition: all 0.25s ease;
}
.slide-enter-from,
.slide-leave-to {
    opacity: 0;
    transform: translateY(-8px);
}
</style>
