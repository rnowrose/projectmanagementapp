<script lang="ts">

    interface CardProps {
        title: string;
        buttonName?: string;
        needsButton: boolean;
        onButtonClick?: () => void;
        // You can define any props you want to pass to the Card component here
    }
    let { title, buttonName, needsButton, onButtonClick }: CardProps = $props();

  // No additional script logic needed for this simple card component
</script>
<div class="card bg-base-100 w-96 shadow-sm">
    <div class="card-body">
        <h2 class="card-title">{title}</h2>
        <slot></slot>
        {#if needsButton}
            <div class="card-actions justify-end">
                <button class="btn btn-primary" onclick={onButtonClick}>{buttonName}</button>
            </div>
        {/if}
    </div>
</div>