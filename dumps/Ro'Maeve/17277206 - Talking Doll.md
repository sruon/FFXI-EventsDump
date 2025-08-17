# 17277206 - Talking Doll

## Common Data

| Field            | Value              |
|------------------|--------------------|
| Zone             | Ro'Maeve (ID: 122) |
| Block Size       | 124 bytes          |
| Total Events     | 3                  |
| References Count | 9                  |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [2](#event-2)         | 0x0001       |     10 |              2 |
| [3](#event-3)         | 0x000B       |     48 |             15 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0267      |         615 |
|       1 | 0xF990      |       63888 |
|       2 | 0xFFFF8D74  |  4294937972 |
|       3 | 0x0C9D      |        3229 |
|       4 | 0x0001      |           1 |
|       5 | 0x1CA7      |        7335 |
|       6 | 0x1CA0      |        7328 |
|       7 | 0x00C8      |         200 |
|       8 | 0x0000      |           0 |

## String References

- **7328**: Ahahahahaha! You're almost on top of it! It's somewhere in this area!
- **7335**: The $0 jumps in your hands.

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

### Event 2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    37 00 80 01 80 02 80  03 80 00                  7.........     
```

#### Opcodes

```
  0: 0x0001 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=0.615*, z=63.888*, y=-29.324*, direction=283.8°*
  1: 0x000A [0x00] END_REQSTACK()
```

### Event 3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000B   |
| Data Size    | 48 bytes |
| Instructions | 15       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                   42 1C 04 80 43             B...C
0010: 00 43 01 1C 04 80 48 05  80 23 1D 06 80 23 4E 00  .C....H..#...#N.
0020: F0 FF FF 7F 46 00 45 07  80 F8 FF FF 7F F8 FF FF  ....F.E.........
0030: 7F 66 64 69 31 08 80 20  00 21 00                 .fdi1.. .!.     
```

#### Opcodes

```
  0: 0x000B [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x000C [0x1C] WAIT(1* ticks)
  2: 0x000F [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  3: 0x0011 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  4: 0x0013 [0x1C] WAIT(1* ticks)
  5: 0x0016 [0x48] [System] [7335*]:
    → "The $0 jumps in your hands."
  6: 0x0019 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x001A [0x1D] PRINT_EVENT_MESSAGE(message_id=7328*)
    → "Ahahahahaha! You're almost on top of it! It's somewhere in this area!"
  8: 0x001D [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x001E [0x4E] SET_ENTITY_HIDE_FLAG: Show LocalPlayer
 10: 0x0024 [0x46] CAMERA_CONTROL: Restore default settings
 11: 0x0026 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [EventEntity, EventEntity], work=[200*, 0*]
 12: 0x0037 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 13: 0x0039 [0x21] END_EVENT
 14: 0x003A [0x00] END_REQSTACK()
```
