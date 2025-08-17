# 17637448 - Changeable

## Common Data

| Field            | Value             |
|------------------|-------------------|
| Zone             | GM_Home (ID: 210) |
| Block Size       | 72 bytes          |
| Total Events     | 3                 |
| References Count | 3                 |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [124](#event-124)     | 0x0001       |     15 |              7 |
| [123](#event-123)     | 0x0010       |     15 |              7 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x001E      |          30 |
|       1 | 0x2337      |        9015 |
|       2 | 0x2338      |        9016 |

## String References

- **9015**: The inn is just up ahead.
- **9016**: The inn? Nowhere around here, I'm afraid.

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

### Event 124

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 15 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    42 1E F0 FF FF 7F 1C  00 80 1D 01 80 23 21 00   B...........#!.
```

#### Opcodes

```
  0: 0x0001 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0002 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0007 [0x1C] WAIT(30* ticks)
  3: 0x000A [0x1D] PRINT_EVENT_MESSAGE(message_id=9015*)
    → "The inn is just up ahead."
  4: 0x000D [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x000E [0x21] END_EVENT
  6: 0x000F [0x00] END_REQSTACK()
```

### Event 123

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0010   |
| Data Size    | 15 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010: 42 1E F0 FF FF 7F 1C 00  80 1D 02 80 23 21 00     B...........#!. 
```

#### Opcodes

```
  0: 0x0010 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0011 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0016 [0x1C] WAIT(30* ticks)
  3: 0x0019 [0x1D] PRINT_EVENT_MESSAGE(message_id=9016*)
    → "The inn? Nowhere around here, I'm afraid."
  4: 0x001C [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x001D [0x21] END_EVENT
  6: 0x001E [0x00] END_REQSTACK()
```
