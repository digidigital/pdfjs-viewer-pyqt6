"""Global stability configuration and environment variable handling.

This module provides functions to configure WebEngine stability settings
at the application level before QApplication is created.
"""

import os
import sys
from typing import List, Optional


def configure_global_stability(
    disable_gpu: bool = True,
    disable_sandbox: bool = False,
    disable_software_rasterizer: bool = False,
    disable_webgl: bool = True,
    disable_gpu_compositing: bool = True,
    single_process: bool = False,
    extra_args: Optional[List[str]] = None
):
    """Configure global WebEngine stability settings.

    IMPORTANT: Must be called BEFORE creating QApplication instance.

    These settings apply globally to all QWebEngine instances in the application.
    For per-viewer settings, use PDFStabilityConfig instead.

    Args:
        disable_gpu: Disable GPU acceleration (recommended for stability)
        disable_sandbox: Disable Chromium sandbox (use cautiously)
        disable_software_rasterizer: Disable software rasterizer fallback
        disable_webgl: Disable WebGL (major crash source)
        disable_gpu_compositing: Disable GPU compositing
        single_process: Run WebEngine in single process mode (less isolation)
        extra_args: Additional Chromium command line arguments

    Example:
        >>> from pdfjs_viewer.stability import configure_global_stability
        >>> configure_global_stability(disable_gpu=True, disable_webgl=True)
        >>> app = QApplication(sys.argv)  # Create app AFTER configuration
    """
    args = []

    if disable_gpu:
        args.extend([
            "--disable-gpu",
            "--disable-software-rasterizer" if disable_software_rasterizer else "",
        ])

    if disable_webgl:
        args.append("--disable-webgl")

    if disable_gpu_compositing:
        args.append("--disable-gpu-compositing")

    if disable_sandbox:
        args.append("--no-sandbox")

    if single_process:
        args.append("--single-process")

    # Add extra args
    if extra_args:
        args.extend(extra_args)

    # Filter empty strings
    args = [arg for arg in args if arg]

    # Set environment variable for QtWebEngine
    if args:
        existing_args = os.environ.get("QTWEBENGINE_CHROMIUM_FLAGS", "")
        if existing_args:
            args = existing_args.split() + args

        os.environ["QTWEBENGINE_CHROMIUM_FLAGS"] = " ".join(args)


def apply_environment_stability():
    """Apply stability settings from environment variables.

    Reads standard QtWebEngine environment variables and applies them.
    Call this BEFORE creating QApplication.

    Supported environment variables:
        QTWEBENGINE_CHROMIUM_FLAGS: Additional Chromium flags
        QTWEBENGINE_DISABLE_SANDBOX: Disable sandbox (1/true/yes)
        PDFJS_VIEWER_SAFER_MODE: Enable safer mode preset (1/true/yes)

    Example:
        >>> from pdfjs_viewer.stability import apply_environment_stability
        >>> apply_environment_stability()
        >>> app = QApplication(sys.argv)
    """
    # Check for safer mode environment variable
    safer_mode = os.environ.get("PDFJS_VIEWER_SAFER_MODE", "").lower() in ("1", "true", "yes")

    if safer_mode:
        configure_global_stability(
            disable_gpu=True,
            disable_webgl=True,
            disable_gpu_compositing=True,
        )

    # Check for sandbox disable
    disable_sandbox = os.environ.get("QTWEBENGINE_DISABLE_SANDBOX", "").lower() in ("1", "true", "yes")

    if disable_sandbox:
        existing_flags = os.environ.get("QTWEBENGINE_CHROMIUM_FLAGS", "")
        if "--no-sandbox" not in existing_flags:
            os.environ["QTWEBENGINE_CHROMIUM_FLAGS"] = f"{existing_flags} --no-sandbox".strip()


def get_recommended_stability_config():
    """Get recommended stability configuration for production use.

    Returns:
        dict: Configuration dict suitable for PDFStabilityConfig
    """
    return {
        "use_isolated_profile": True,
        "disable_webgl": True,
        "disable_gpu": True,
        "disable_gpu_compositing": True,
        "disable_cache": True,
        "disable_local_storage": True,
        "disable_service_workers": True,
        "disable_background_networking": True,
        "safer_mode": True,
    }


def get_maximum_stability_config():
    """Get maximum stability configuration (most restrictive).

    This configuration disables all non-essential features for maximum stability.
    Use when crashes are frequent or in production environments.

    Returns:
        dict: Configuration dict suitable for PDFStabilityConfig
    """
    return {
        "use_isolated_profile": True,
        "disable_webgl": True,
        "disable_gpu": True,
        "disable_gpu_compositing": True,
        "disable_cache": True,
        "disable_local_storage": True,
        "disable_session_storage": True,
        "disable_databases": True,
        "disable_service_workers": True,
        "disable_background_networking": True,
        "disable_software_rasterizer": False,  # Keep software rendering
        "max_cache_size_mb": 0,
        "safer_mode": True,
    }


def print_stability_info():
    """Print current stability configuration to stdout.

    Useful for debugging and verifying configuration.
    """
    print("=== WebEngine Stability Configuration ===")
    print(f"QTWEBENGINE_CHROMIUM_FLAGS: {os.environ.get('QTWEBENGINE_CHROMIUM_FLAGS', '(not set)')}")
    print(f"QTWEBENGINE_DISABLE_SANDBOX: {os.environ.get('QTWEBENGINE_DISABLE_SANDBOX', '(not set)')}")
    print(f"PDFJS_VIEWER_SAFER_MODE: {os.environ.get('PDFJS_VIEWER_SAFER_MODE', '(not set)')}")
    print("=========================================")
