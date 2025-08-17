# 17891738 - Inlet of Whispers

## Common Data

| Field            | Value               |
|------------------|---------------------|
| Zone             | Dho Gates (ID: 272) |
| Block Size       | 148 bytes           |
| Total Events     | 3                   |
| References Count | 6                   |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [17](#event-17)       | 0x0001       |     94 |             16 |
| [18](#event-18)       | 0x005F       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x005A      |          90 |
|       2 | 0x0004      |           4 |
|       3 | 0x026A      |         618 |
|       4 | 0x1E7C      |        7804 |
|       5 | 0x03E7      |         999 |

## String References

- **7804**: A bittersweet breeze of melancholy and remembrance graces the air about you for one fleeting moment.

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

### Event 17

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 94 bytes |
| Instructions | 16       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    42 6A 00 80 01 80 02  80 4A F0 FF FF 7F F8 FF   Bj......J......
0010: FF 7F 6F 76 F0 FF FF 7F  29 08 F0 FF FF 7F 04 2A  ..ov....)......*
0020: 08 F0 FF FF 7F 45 03 80  F8 FF FF 7F F8 FF FF 7F  .....E..........
0030: 73 30 39 36 00 80 55 03  80 F8 FF FF 7F F8 FF FF  s096..U.........
0040: 7F 73 30 39 36 48 04 80  23 6A 05 80 01 80 02 80  .s096H..#j......
0050: 29 08 F0 FF FF 7F 05 2A  08 F0 FF FF 7F 21 00     )......*.....!. 
```

#### Opcodes

```
  0: 0x0001 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0002 [0x6A] CHANGE_SOUND_VOLUME: Set (Zone)* volume to 0*, fade_time=90*
  2: 0x0009 [0x4A] LocalPlayer looks at EventEntity
  3: 0x0012 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0013 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until LocalPlayer Render.Flags0 and Render.Flags3 conditions are met
  5: 0x0018 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=LocalPlayer, tag_num=0x04)
  6: 0x001F [0x2A] GET_REQ_LEVEL(level=8, entity_id=LocalPlayer)
  7: 0x0025 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s096" with entities [EventEntity, EventEntity], work=[618*, 0*]
  8: 0x0036 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "s096" with entities [EventEntity, EventEntity], work=618*
  9: 0x0045 [0x48] [System] [7804*]:
    → "A bittersweet breeze of melancholy and remembrance graces the air about you for one fleeting moment."
 10: 0x0048 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x0049 [0x6A] CHANGE_SOUND_VOLUME: Set (Zone)* volume to 999*, fade_time=90*
 12: 0x0050 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=LocalPlayer, tag_num=0x05)
 13: 0x0057 [0x2A] GET_REQ_LEVEL(level=8, entity_id=LocalPlayer)
 14: 0x005D [0x21] END_EVENT
 15: 0x005E [0x00] END_REQSTACK()
```

### Event 18

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x005F  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                               00                 .
```

#### Opcodes

```
  0: 0x005F [0x00] END_REQSTACK()
```
