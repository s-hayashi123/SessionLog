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
    form.memo = ""
    await refreshNuxtData()
}
</script>

<template>
    <div>
        <!-- Back Link -->
        <NuxtLink to="/members" class="inline-flex items-center gap-1 text-sm text-text-muted hover:text-accent transition-colors mb-4">
            ‹ 会員一覧
        </NuxtLink>

        <!-- Member Profile Card -->
        <div class="bg-surface-raised border border-border-subtle rounded-xl p-5 mb-6">
            <h2 class="text-xl font-700 text-text-primary mb-3">{{ member?.name }}</h2>
            <div class="grid grid-cols-3 gap-3">
                <div class="bg-input-bg rounded-lg p-3 text-center">
                    <p class="text-xs text-text-muted mb-1">年齢</p>
                    <p class="text-lg font-600 text-text-primary">{{ member?.age }}<span class="text-xs text-text-muted ml-0.5">歳</span></p>
                </div>
                <div class="bg-input-bg rounded-lg p-3 text-center">
                    <p class="text-xs text-text-muted mb-1">体重</p>
                    <p class="text-lg font-600 text-text-primary">{{ member?.weight }}<span class="text-xs text-text-muted ml-0.5">kg</span></p>
                </div>
                <div class="bg-input-bg rounded-lg p-3 text-center">
                    <p class="text-xs text-text-muted mb-1">体脂肪</p>
                    <p class="text-lg font-600 text-text-primary">{{ member?.body_fat }}<span class="text-xs text-text-muted ml-0.5">%</span></p>
                </div>
            </div>
            <p class="text-xs text-text-muted mt-3">入会日: {{ member?.joined_at?.slice(0, 10) }}</p>
        </div>

        <!-- New Session Form -->
        <div class="mb-6">
            <p class="text-xs text-text-muted uppercase tracking-widest font-500 mb-2">新規セッション</p>
            <form @submit.prevent="createSession" class="flex gap-2">
                <input v-model="form.memo" placeholder="メモ（任意）"
                    class="flex-1 bg-input-bg border border-input-border rounded-lg px-4 py-2.5 text-text-primary placeholder:text-text-muted focus:outline-none focus:border-input-focus transition-colors" />
                <button type="submit"
                    class="bg-accent text-surface font-600 text-sm px-5 py-2.5 rounded-lg hover:bg-accent-hover transition-all cursor-pointer active:scale-95 shrink-0">
                    記録
                </button>
            </form>
        </div>

        <!-- Sessions List -->
        <div>
            <div class="flex items-center justify-between mb-3">
                <p class="text-xs text-text-muted uppercase tracking-widest font-500">セッション履歴</p>
                <p class="text-xs text-text-muted">{{ sessions?.length || 0 }} 件</p>
            </div>
            <ul class="space-y-2">
                <li v-for="session in sessions" :key="session.session_date">
                    <NuxtLink :to="`/members/${route.params.id}/sessions/${session.session_date}`"
                        class="flex items-center justify-between bg-surface-raised border border-border-subtle rounded-xl px-5 py-4 hover:bg-surface-hover hover:border-accent/30 transition-all group">
                        <div>
                            <p class="font-500 text-text-primary text-sm">{{ session.session_date }}</p>
                            <p v-if="session.memo" class="text-xs text-text-muted mt-0.5">{{ session.memo }}</p>
                        </div>
                        <span class="text-text-muted group-hover:text-accent transition-colors text-lg">›</span>
                    </NuxtLink>
                </li>
            </ul>
            <p v-if="!sessions?.length" class="text-center text-text-muted py-12 text-sm">
                まだセッションが記録されていません
            </p>
        </div>
    </div>
</template>
