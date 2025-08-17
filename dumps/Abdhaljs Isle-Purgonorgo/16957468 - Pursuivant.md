# 16957468 - Pursuivant

## Common Data

| Field            | Value                             |
|------------------|-----------------------------------|
| Zone             | Abdhaljs Isle-Purgonorgo (ID: 44) |
| Block Size       | 64 bytes                          |
| Total Events     | 2                                 |
| References Count | 3                                 |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [16](#event-16)       | 0x0001       |     26 |              8 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1D20      |        7456 |
|       1 | 0x0003      |           3 |
|       2 | 0x00E6      |         230 |

## String References

- **7456**: Back into the breach, <Player>!

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

### Event 16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 26 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    42 1E F0 FF FF 7F 1D  00 80 23 73 01 80 F8 FF   B........#s....
0010: FF 7F F0 FF FF 7F 1C 02  80 21 00                 .........!.     
```

#### Opcodes

```
  0: 0x0001 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0002 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0007 [0x1D] PRINT_EVENT_MESSAGE(message_id=7456*)
    → "Back into the breach, <Player>!"
  3: 0x000A [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x000B [0x73] EventEntity casts magic 3* on LocalPlayer
  5: 0x0016 [0x1C] WAIT(230* ticks)
  6: 0x0019 [0x21] END_EVENT
  7: 0x001A [0x00] END_REQSTACK()
```
