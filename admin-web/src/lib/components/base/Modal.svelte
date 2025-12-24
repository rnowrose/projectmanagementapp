<script lang="ts">
    interface Props {
        title: string;
    }

    let  { title } = $props();
</script>

<div class="modal-box rounded-box border p-0 w-100 max-w-2xl">
     <div class="bg-primary text-primary-content rounded-t-box flex items-center justify-between">
        <h3 class="font-bold text-lg p-1">{title}</h3>
        <form method="dialog">
            <button class="btn btn-sm btn-circle btn-ghost">✕</button>
        </form>
    </div>
    <slot></slot>
</div>