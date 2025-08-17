# 17723490 - Bertenont

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Northern San d'Oria (ID: 231) |
| Block Size       | 100 bytes                     |
| Total Events     | 2                             |
| References Count | 5                             |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [809](#event-809)     | 0x0001       |     52 |             12 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x37EF      |       14319 |
|       1 | 0x001E      |          30 |
|       2 | 0x0014      |          20 |
|       3 | 0x37FE      |       14334 |
|       4 | 0x37FF      |       14335 |

## String References

- **14319**: <Player>'s badge flashes brightly.
- **14334**: Oh my, I thought a shooting star had crossed my vision for a moment there. I believe I just made a wish on your badge, [good sir/madame].
- **14335**: It comes from the Near East, you say? Such a captivating shine it has. I wonder if the stars in that nation burn as brightly as they do here? Perhaps I shall go and see for myself...

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

### Event 809

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 52 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    42 48 00 80 1E F0 FF  FF 7F 1C 01 80 66 02 80   BH..........f..
0010: F8 FF FF 7F F8 FF FF 7F  74 6C 6B 30 1D 03 80 23  ........tlk0...#
0020: 66 02 80 F8 FF FF 7F F8  FF FF 7F 74 6C 6B 31 1D  f..........tlk1.
0030: 04 80 23 21 00                                    ..#!.           
```

#### Opcodes

```
  0: 0x0001 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0002 [0x48] [System] [14319*]:
    → "<Player>'s badge flashes brightly."
  2: 0x0005 [0x1E] EventEntity looks at LocalPlayer and starts talking
  3: 0x000A [0x1C] WAIT(30* ticks)
  4: 0x000D [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
  5: 0x001C [0x1D] PRINT_EVENT_MESSAGE(message_id=14334*)
    → "Oh my, I thought a shooting star had crossed my vision for a moment there. I believe I just made a wish on your badge, [good sir/madame]."
  6: 0x001F [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0020 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=20*
  8: 0x002F [0x1D] PRINT_EVENT_MESSAGE(message_id=14335*)
    → "It comes from the Near East, you say? Such a captivating shine it has. I wonder if the stars in that nation burn as brightly as they do here? Perhaps I shall go and see for myself..."
  9: 0x0032 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x0033 [0x21] END_EVENT
 11: 0x0034 [0x00] END_REQSTACK()
```
