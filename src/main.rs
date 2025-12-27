slint::include_modules!();

fn main() -> Result<(), slint::PlatformError> {
    std::env::set_var(
        "SLINT_DEBUG_PERFORMANCE",
        "refresh_full_speed,overlay,console",
    );

    let ui = AppWindow::new()?;
    ui.run()
}
