<script setup lang="ts">
const route = useRoute()
const config = useRuntimeConfig()
const base = config.public.apiBase
const editing = ref(false)
const editForm = reactive({ name: "", age: 0, gender: "", height: 0, weight: 0, body_fat: 0, memo: "" })

import type { Member, Session } from '../../../types'

const { data: member } = await useFetch<Member>(`${base}/members/${route.params.id}`)
const { data: sessions } = await useFetch<Session[]>(`${base}/members/${route.params.id}/sessions`)
const form = reactive({ duration: 0, weight: 0, body_fat: 0, memo: "" })

const createSession = async () => {
    await $fetch(`${base}/members/${route.params.id}/sessions`, {
        method: "POST",
        body: form
    })
    form.duration = 0
    form.weight = 0
    form.body_fat = 0
    form.memo = ""
    await refreshNuxtData()
}

const startEdit = () => {
    if (member.value) {
        Object.assign(editForm, {
            name: member.value.name,
            age: member.value.age,
            gender: member.value.gender,
            height: member.value.height,
            weight: member.value.weight,
            body_fat: member.value.body_fat,
            memo: member.value.memo || ""
        })
    }
    editing.value = true
}

const updateMember = async () => {
    await $fetch(`${base}/members/${route.params.id}`, {
        method: "PUT",
        body: editForm
    })
    editing.value = false
    await refreshNuxtData()
}
</script>

<template>
    <div>
        <!-- Back Link -->
        <NuxtLink to="/members"
            class="inline-flex items-center gap-1 text-sm text-text-muted hover:text-accent transition-colors mb-4">
            ‹ 会員一覧
        </NuxtLink>

        <!-- Member Profile Card -->
        <div class="bg-surface-raised border border-border-subtle rounded-xl p-5 mb-6">
            <div class="flex items-center justify-between mb-3">
                <h2 class="text-xl font-700 text-text-primary">{{ member?.name }}</h2>
                <button v-if="!editing" @click="startEdit"
                    class="text-xs text-text-muted hover:text-accent transition-colors cursor-pointer">
                    編集
                </button>
            </div>

            <!-- 表示モード -->
            <template v-if="!editing">
                <div class="grid grid-cols-3 gap-3">
                    <div class="bg-input-bg rounded-lg p-3 text-center">
                        <p class="text-xs text-text-muted mb-1">年齢</p>
                        <p class="text-lg font-600 text-text-primary">{{ member?.age }}<span
                                class="text-xs text-text-muted ml-0.5">歳</span></p>
                    </div>
                    <div class="bg-input-bg rounded-lg p-3 text-center">
                        <p class="text-xs text-text-muted mb-1">体重</p>
                        <p class="text-lg font-600 text-text-primary">{{ member?.weight }}<span
                                class="text-xs text-text-muted ml-0.5">kg</span></p>
                    </div>
                    <div class="bg-input-bg rounded-lg p-3 text-center">
                        <p class="text-xs text-text-muted mb-1">体脂肪</p>
                        <p class="text-lg font-600 text-text-primary">{{ member?.body_fat }}<span
                                class="text-xs text-text-muted ml-0.5">%</span></p>
                    </div>
                </div>
                <p class="text-xs text-text-muted mt-3">入会日: {{ member?.joined_at?.slice(0, 10) }}</p>
            </template>

            <!-- 編集モード -->
            <form v-else @submit.prevent="updateMember" class="space-y-3">
                <input v-model="editForm.name" placeholder="名前" required
                    class="w-full bg-input-bg border border-input-border rounded-lg px-4 py-2.5 text-text-primary focus:outline-none focus:border-input-focus transition-colors" />
                <div class="grid grid-cols-2 gap-3">
                    <input v-model="editForm.age" placeholder="年齢" type="number" required
                        class="bg-input-bg border border-input-border rounded-lg px-4 py-2.5 text-text-primary focus:outline-none focus:border-input-focus transition-colors" />
                    <select v-model="editForm.gender" required
                        class="bg-input-bg border border-input-border rounded-lg px-4 py-2.5 text-text-primary focus:outline-none focus:border-input-focus transition-colors">
                        <option value="男性">男性</option>
                        <option value="女性">女性</option>
                        <option value="その他">その他</option>
                    </select>
                </div>
                <div class="grid grid-cols-3 gap-3">
                    <input v-model="editForm.height" placeholder="身長" type="number" step="0.1" required
                        class="bg-input-bg border border-input-border rounded-lg px-4 py-2.5 text-text-primary focus:outline-none focus:border-input-focus transition-colors" />
                    <input v-model="editForm.weight" placeholder="体重" type="number" step="0.1" required
                        class="bg-input-bg border border-input-border rounded-lg px-4 py-2.5 text-text-primary focus:outline-none focus:border-input-focus transition-colors" />
                    <input v-model="editForm.body_fat" placeholder="体脂肪" type="number" step="0.1" required
                        class="bg-input-bg border border-input-border rounded-lg px-4 py-2.5 text-text-primary focus:outline-none focus:border-input-focus transition-colors" />
                </div>
                <input v-model="editForm.memo" placeholder="メモ"
                    class="w-full bg-input-bg border border-input-border rounded-lg px-4 py-2.5 text-text-primary placeholder:text-text-muted focus:outline-none focus:border-input-focus transition-colors" />
                <div class="flex gap-2">
                    <button type="submit"
                        class="flex-1 bg-accent text-surface font-600 rounded-lg py-2.5 hover:bg-accent-hover transition-all cursor-pointer">
                        保存
                    </button>
                    <button type="button" @click="editing = false"
                        class="flex-1 bg-surface-hover text-text-secondary font-600 rounded-lg py-2.5 hover:bg-border-subtle transition-all cursor-pointer">
                        キャンセル
                    </button>
                </div>
            </form>
        </div>

        <!-- New Session Form -->
        <div class="mb-6">
            <p class="text-xs text-text-muted uppercase tracking-widest font-500 mb-2">新規セッション</p>
            <form @submit.prevent="createSession"
                class="bg-surface-raised border border-border-subtle rounded-xl p-5 space-y-3">
                <div class="grid grid-cols-3 gap-3">
                    <div>
                        <label class="text-[10px] text-text-muted uppercase tracking-wider block mb-1">時間(分)</label>
                        <input v-model="form.duration" type="number"
                            class="w-full bg-input-bg border border-input-border rounded-lg px-3 py-2.5 text-text-primary text-center focus:outline-none focus:border-input-focus transition-colors" />
                    </div>
                    <div>
                        <label class="text-[10px] text-text-muted uppercase tracking-wider block mb-1">体重(kg)</label>
                        <input v-model="form.weight" type="number" step="0.1"
                            class="w-full bg-input-bg border border-input-border rounded-lg px-3 py-2.5 text-text-primary text-center focus:outline-none focus:border-input-focus transition-colors" />
                    </div>
                    <div>
                        <label class="text-[10px] text-text-muted uppercase tracking-wider block mb-1">体脂肪(%)</label>
                        <input v-model="form.body_fat" type="number" step="0.1"
                            class="w-full bg-input-bg border border-input-border rounded-lg px-3 py-2.5 text-text-primary text-center focus:outline-none focus:border-input-focus transition-colors" />
                    </div>
                </div>
                <input v-model="form.memo" placeholder="メモ（任意）"
                    class="w-full bg-input-bg border border-input-border rounded-lg px-4 py-2.5 text-text-primary placeholder:text-text-muted focus:outline-none focus:border-input-focus transition-colors" />
                <button type="submit"
                    class="w-full bg-accent text-surface font-600 rounded-lg py-2.5 hover:bg-accent-hover transition-all cursor-pointer active:scale-[0.98]">
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
