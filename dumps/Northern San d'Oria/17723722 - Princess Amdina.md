# 17723722 - Princess Amdina

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Northern San d'Oria (ID: 231) |
| Block Size       | 56 bytes                      |
| Total Events     | 2                             |
| References Count | 2                             |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [854](#event-854)     | 0x0001       |     20 |             10 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x442F      |       17455 |
|       1 | 0x4430      |       17456 |

## String References

- **17455**: It is our fervent hope that thou hast thoroughly enjoyed the Celestial Nights event.
- **17456**: We present this gift to thee, as a token of our gratitude for thine unrelenting support.

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

### Event 854

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 20 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 42 1E F0 FF FF  7F 1D 00 80 23 1D 01 80    .B........#...
0010: 23 20 00 21 00                                    # .!.           
```

#### Opcodes

```
  0: 0x0001 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0003 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0004 [0x1E] EventEntity looks at LocalPlayer and starts talking
  3: 0x0009 [0x1D] PRINT_EVENT_MESSAGE(message_id=17455*)
    → "It is our fervent hope that thou hast thoroughly enjoyed the Celestial Nights event."
  4: 0x000C [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x000D [0x1D] PRINT_EVENT_MESSAGE(message_id=17456*)
    → "We present this gift to thee, as a token of our gratitude for thine unrelenting support."
  6: 0x0010 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0011 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  8: 0x0013 [0x21] END_EVENT
  9: 0x0014 [0x00] END_REQSTACK()
```
