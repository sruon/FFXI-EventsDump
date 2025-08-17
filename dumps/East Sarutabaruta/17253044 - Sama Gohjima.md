# 17253044 - Sama Gohjima

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | East Sarutabaruta (ID: 116) |
| Block Size       | 68 bytes                    |
| Total Events     | 3                           |
| References Count | 2                           |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [43](#event-43)       | 0x0001       |     15 |              8 |
| [53](#event-53)       | 0x0010       |     15 |              8 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1CF1      |        7409 |
|       1 | 0x1CF2      |        7410 |

## String References

- **7409**: This is the east magic towerrr. Beneath here lies the Horutoto Ruins that have existed here in Sarutabaruta long beforrre Windurst even came into existence.
- **7410**: The ministerrr of the Orastery is in the laborrratory beneath here. To get there, you should check the walls verrry carrrefully.

## Events

### Event 65535

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0000  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 00                                                .               
```

#### Opcodes

```
  0: 0x0000 [0x00] END_REQSTACK()
```

### Event 43

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 15 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  1D 00 80 23 20 00 21 00   .....op...# .!.
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x1D] PRINT_EVENT_MESSAGE(message_id=7409*)
    → "This is the east magic towerrr. Beneath here lies the Horutoto Ruins that have existed here in Sarutabaruta long beforrre Windurst even came into existence."
  4: 0x000B [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x000C [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  6: 0x000E [0x21] END_EVENT
  7: 0x000F [0x00] END_REQSTACK()
```

### Event 53

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0010   |
| Data Size    | 15 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010: 1E F0 FF FF 7F 6F 70 1D  01 80 23 20 00 21 00     .....op...# .!. 
```

#### Opcodes

```
  0: 0x0010 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0015 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0016 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0017 [0x1D] PRINT_EVENT_MESSAGE(message_id=7410*)
    → "The ministerrr of the Orastery is in the laborrratory beneath here. To get there, you should check the walls verrry carrrefully."
  4: 0x001A [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x001B [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  6: 0x001D [0x21] END_EVENT
  7: 0x001E [0x00] END_REQSTACK()
```
