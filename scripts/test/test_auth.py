# SPDX-FileCopyrightText: 2026 Epic Games, Inc.
# SPDX-License-Identifier: MIT
import logging

import pytest
from error_types import NotSupportedError

from lore import Lore

logger = logging.getLogger(__name__)


@pytest.mark.smoke
def test_auth_login_not_supported_without_auth_endpoint(new_lore_repo):
    """The local test server is authless (no auth endpoint configured), so an
    interactive `auth login` against it must fail with `NotSupported` rather
    than an opaque internal error."""

    repo: Lore = new_lore_repo()

    with pytest.raises(NotSupportedError):
        repo.run(urc_args=["auth", "login", repo.remote_path, "--no-browser"])


@pytest.mark.smoke
def test_auth_info_not_supported_without_auth_endpoint(new_lore_repo):
    """`auth info` resolves its auth endpoint from the repository's remote. The
    authless test server advertises no auth endpoint, so there is no URL to key
    a token lookup on and the command must fail with `NotSupported`."""

    repo: Lore = new_lore_repo()

    with pytest.raises(NotSupportedError):
        repo.run(urc_args=["auth", "info"])
