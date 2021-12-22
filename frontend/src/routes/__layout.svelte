<script lang="ts">
	// Bulma import
	import 'bulma/bulma.sass';
	// Tooltip extension
	import '@creativebulma/bulma-tooltip/dist/bulma-tooltip.css';
	// Override the css
	import '../app.scss';
</script>

<slot />

<style global>
	ion-icon {
		visibility: inherit !important;
	}
</style>
