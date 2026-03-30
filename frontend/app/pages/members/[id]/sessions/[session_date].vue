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
    form.exercise_id = ""
    form.sets = 0
    form.reps = 0
    form.weight = 0
    await refreshNuxtData()
}

import type { Session, SessionDetail } from '../../../../types'

const { data: sessions } = await useFetch<Session[]>(`${base}/members/${route.params.id}/sessions`)
const session = computed(() => sessions.value?.find(s => s.session_date === route.params.session_date))
const { data: details } = await useFetch<SessionDetail[]>(`${base}/members/${route.params.id}/sessions/${route.params.session_date}/details`)
</script>

<template>
    <div>
        <!-- Back Link -->
        <NuxtLink :to="`/members/${route.params.id}`"
            class="inline-flex items-center gap-1 text-sm text-text-muted hover:text-accent transition-colors mb-4">
            ‹ 戻る
        </NuxtLink>

        <!-- Session Header -->
        <div class="bg-surface-raised border border-border-subtle rounded-xl p-5 mb-6">
            <p class="text-xs text-text-muted uppercase tracking-widest font-500 mb-1">セッション日</p>
            <h2 class="text-xl font-700 text-text-primary mb-3">{{ route.params.session_date }}</h2>
            <div class="grid grid-cols-2 gap-3" v-if="session?.weight || session?.body_fat">
                <div class="bg-input-bg rounded-lg p-3 text-center">
                    <p class="text-xs text-text-muted mb-1">体重</p>
                    <p class="text-lg font-600 text-text-primary">{{ session?.weight ?? '-' }}<span class="text-xs text-text-muted ml-0.5">kg</span></p>
                </div>
                <div class="bg-input-bg rounded-lg p-3 text-center">
                    <p class="text-xs text-text-muted mb-1">体脂肪</p>
                    <p class="text-lg font-600 text-text-primary">{{ session?.body_fat ?? '-' }}<span class="text-xs text-text-muted ml-0.5">%</span></p>
                </div>
            </div>
        </div>

        <!-- Add Exercise Form -->
        <div class="mb-6">
            <p class="text-xs text-text-muted uppercase tracking-widest font-500 mb-2">種目を追加</p>
            <form @submit.prevent="createDetail"
                class="bg-surface-raised border border-border-subtle rounded-xl p-5 space-y-3">
                <input v-model="form.exercise_id" placeholder="種目名" required
                    class="w-full bg-input-bg border border-input-border rounded-lg px-4 py-2.5 text-text-primary placeholder:text-text-muted focus:outline-none focus:border-input-focus transition-colors" />
                <div class="grid grid-cols-3 gap-3">
                    <div>
                        <label class="text-[10px] text-text-muted uppercase tracking-wider block mb-1">セット</label>
                        <input v-model="form.sets" type="number" required
                            class="w-full bg-input-bg border border-input-border rounded-lg px-3 py-2.5 text-text-primary text-center focus:outline-none focus:border-input-focus transition-colors" />
                    </div>
                    <div>
                        <label class="text-[10px] text-text-muted uppercase tracking-wider block mb-1">レップ</label>
                        <input v-model="form.reps" type="number" required
                            class="w-full bg-input-bg border border-input-border rounded-lg px-3 py-2.5 text-text-primary text-center focus:outline-none focus:border-input-focus transition-colors" />
                    </div>
                    <div>
                        <label class="text-[10px] text-text-muted uppercase tracking-wider block mb-1">重量kg</label>
                        <input v-model="form.weight" type="number" step="0.25" required
                            class="w-full bg-input-bg border border-input-border rounded-lg px-3 py-2.5 text-text-primary text-center focus:outline-none focus:border-input-focus transition-colors" />
                    </div>
                </div>
                <button type="submit"
                    class="w-full bg-accent text-surface font-600 rounded-lg py-2.5 hover:bg-accent-hover transition-all cursor-pointer active:scale-[0.98]">
                    追加
                </button>
            </form>
        </div>

        <!-- Exercise List -->
        <div>
            <div class="flex items-center justify-between mb-3">
                <p class="text-xs text-text-muted uppercase tracking-widest font-500">セッション内容</p>
                <p class="text-xs text-text-muted">{{ details?.length || 0 }} 種目</p>
            </div>
            <ul class="space-y-2">
                <li v-for="detail in details" :key="detail.exercise_id"
                    class="bg-surface-raised border border-border-subtle rounded-xl px-5 py-4">
                    <p class="font-600 text-text-primary mb-2">{{ detail.exercise_id }}</p>
                    <div class="flex gap-4 text-sm">
                        <span class="text-text-secondary">
                            <span class="text-accent font-600">{{ detail.sets }}</span>
                            <span class="text-text-muted ml-0.5">sets</span>
                        </span>
                        <span class="text-text-secondary">
                            <span class="text-accent font-600">{{ detail.reps }}</span>
                            <span class="text-text-muted ml-0.5">reps</span>
                        </span>
                        <span class="text-text-secondary">
                            <span class="text-accent font-600">{{ detail.weight }}</span>
                            <span class="text-text-muted ml-0.5">kg</span>
                        </span>
                    </div>
                </li>
            </ul>
            <p v-if="!details?.length" class="text-center text-text-muted py-12 text-sm">
                まだ種目が追加されていません
            </p>
        </div>
    </div>
</template>
