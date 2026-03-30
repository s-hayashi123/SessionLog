<script setup lang="ts">
</script>

<template>
    <div class="min-h-screen bg-surface">
        <header class="border-b border-border-subtle bg-surface-raised/80 backdrop-blur-md sticky top-0 z-50">
            <div class="max-w-lg mx-auto px-5 py-4 flex items-center justify-between">
                <NuxtLink to="/members" class="flex items-center gap-2 group">
                    <span
                        class="text-accent text-2xl font-800 tracking-tight group-hover:text-accent-hover transition-colors">
                        Session<span class="text-text-primary">Log</span>
                    </span>
                </NuxtLink>
                <span class="text-[10px] text-text-muted uppercase tracking-[0.2em] font-500">Session Logger</span>
            </div>
        </header>

        <main class="max-w-lg mx-auto px-5 py-6">
            <slot />
        </main>
    </div>
</template>
