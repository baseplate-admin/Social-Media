<script lang="ts">
	import logo from '$lib/assets/img/logo.avif';
</script>

<svelte:head>
	<link
		async
		defer
		rel="stylesheet"
		href="https://cdn.jsdelivr.net/npm/typeface-cantarell@1.1.13/index.min.css"
	/>
	<link
		async
		defer
		rel="stylesheet"
		href="https://cdn.jsdelivr.net/npm/typeface-ubuntu@1.1.13/index.min.css"
	/>
</svelte:head>
<section class="hero is-fullheight">
	<div class="hero-body">
		<div class="container">
			<div class="columns is-centered is-desktop">
				<div
					class="
                        column
                        is-half-desktop is-full-mobile is-narrow-tablet
                    "
				>
					<div class="icon-box box">
						<div class="columns is-mobile is-centered">
							<div class="column is-narrow">
								<img
									src={logo}
									alt="logo"
									style="width: 150px; height: 40px"
									width="150"
									height="40"
								/>
							</div>
						</div>
					</div>
					<div class="box form-box">
						<slot />
					</div>
				</div>
			</div>
		</div>
	</div>
</section>

<style global lang="scss">
	// Overide
	[data-tooltip]::before {
		color: white !important;
		background-color: black !important;
		border: 1px solid #ffffffcf !important;
	}
	[data-tooltip]:not(.is-disabled).has-tooltip-right.has-tooltip-arrow::after,
	[data-tooltip]:not(.is-loading).has-tooltip-right.has-tooltip-arrow::after,
	[data-tooltip]:not([disabled]).has-tooltip-right.has-tooltip-arrow::after {
		top: auto;
		right: 0;
		bottom: 50%;
		left: auto;
		margin: auto -6px -6px auto;
		border-color: transparent rgba(255, 255, 255, 0.9) transparent transparent;
	}
	[data-tooltip]:not(.is-disabled).has-tooltip-left.has-tooltip-arrow::after,
	[data-tooltip]:not(.is-loading).has-tooltip-left.has-tooltip-arrow::after,
	[data-tooltip]:not([disabled]).has-tooltip-left.has-tooltip-arrow::after {
		top: auto;
		right: auto;
		bottom: 50%;
		left: 0;
		margin: auto auto -6px -5px;
		border-color: transparent transparent transparent rgba(255, 255, 255, 0.9);
	}

	// Css has to be global here because the child components use this exact css

	.hero-body {
		.container {
			.columns {
				.column {
					.icon-box {
						background-color: transparent;
					}

					.form-box {
						background-color: transparent;
						border: 1.95px solid var(--border-color);
						/*================================================*/
						// A little override to get tooltip.
						.data-tooltip-hidden {
							&::before {
								visibility: hidden !important;
							}
						}
						[data-tooltip] {
							&::before {
								color: white !important;
								background-color: black !important;
								border: 1px solid #434343 !important;
							}
						}
						/*================================================*/

						.items {
							padding: 0.4em;
						}

						.input {
							background-color: transparent;
							border: 1px solid var(--border-color);
							color: white;

							&.error {
								box-shadow: 0 0 0 0.125em rgba(199, 72, 72, 0.25) !important;
							}

							&::placeholder {
								color: white;
								opacity: 0.75;
								font-family: 'Ubuntu';
							}
						}

						.button {
							border-color: var(--button-border-color) !important;
							border-width: 1.8px;
							text-decoration: none !important;
							color: hsl(0, 0%, 85%) !important;
							transition: 0.2s;

							&:hover {
								background-color: var(--button-color-hover) !important;
							}
						}

						.level {
							transition: 0.2s;
						}
						.new_here_tag {
							font-family: 'Cantarell';
							color: white;
							opacity: 0.85;
						}

						.href_tag {
							text-decoration: none;
							font-family: 'Cantarell';

							&:hover {
								text-decoration: underline;
							}
						}
					}
				}
			}
		}
	}
</style>
