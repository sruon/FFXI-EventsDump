# 17797154 - Celestina

## Common Data

| Field            | Value            |
|------------------|------------------|
| Zone             | Mhaura (ID: 249) |
| Block Size       | 344 bytes        |
| Total Events     | 6                |
| References Count | 16               |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [124](#event-124)        | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     31 |              9 |
| [65535.2](#event-655352) | 0x0021       |     25 |              5 |
| [65535.3](#event-655353) | 0x003A       |     16 |              2 |
| [65535.4](#event-655354) | 0x004A       |    163 |             23 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0x1B3F      |        6975 |
|       2 | 0x5337      |       21303 |
|       3 | 0xA19D      |       41373 |
|       4 | 0xFFFFE1AC  |  4294959532 |
|       5 | 0x000A      |          10 |
|       6 | 0x1B40      |        6976 |
|       7 | 0x003C      |          60 |
|       8 | 0x1B43      |        6979 |
|       9 | 0x0B23      |        2851 |
|      10 | 0x000B      |          11 |
|      11 | 0x1B44      |        6980 |
|      12 | 0x0028      |          40 |
|      13 | 0x436E      |       17262 |
|      14 | 0xB1F6      |       45558 |
|      15 | 0xFFFFE0B8  |  4294959288 |

## String References

- **6975**: Mother? You're here again!?
- **6976**: I know how you feel, Mother, but you have to let him go!
- **6979**: Mother! How long have you been saying that!?
- **6980**: Just stop it! I don't want to hear it anymore!

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

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    00                                              .              
```

#### Opcodes

```
  0: 0x0001 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 31 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       22 00 2F 00 22 90  0F 01 32 00 80 1D 01 80    "./."...2.....
0010: 1F 00 02 80 03 80 04 80  1F 01 1E 21 90 0F 01 23  ...........!...#
0020: 00                                                .               
```

#### Opcodes

```
  0: 0x0002 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0004 [0x2F] Celestina (ID: 17797154/0x010F9022)->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x000A [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  3: 0x000D [0x1D] PRINT_EVENT_MESSAGE(message_id=6975*)
    → "Mother? You're here again!?"
  4: 0x0010 [0x1F] MOVE_ENTITY: EventEntity moves to X=21.303*, Z=41.373*, Y=-7.764*
  5: 0x0018 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  6: 0x001A [0x1E] EventEntity looks at Blandine (ID: 17797153/0x010F9021) and starts talking
  7: 0x001F [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0020 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0021   |
| Data Size    | 25 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:    66 05 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 30   f..........tlk0
0030: 1D 06 80 23 5E 69 64 6C  30 00                    ...#^idl0.      
```

#### Opcodes

```
  0: 0x0021 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=10*
  1: 0x0030 [0x1D] PRINT_EVENT_MESSAGE(message_id=6976*)
    → "I know how you feel, Mother, but you have to let him go!"
  2: 0x0033 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0034 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  4: 0x0039 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003A   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                66 05 80 F8 FF FF            f.....
0040: 7F F8 FF FF 7F 74 68 6B  31 00                    .....thk1.      
```

#### Opcodes

```
  0: 0x003A [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=10*
  1: 0x0049 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x004A    |
| Data Size    | 163 bytes |
| Instructions | 23        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                53 F8 FF FF 7F F8            S.....
0050: FF FF 7F 74 68 6B 31 66  05 80 F8 FF FF 7F F8 FF  ...thk1f........
0060: FF 7F 74 68 6B 32 53 F8  FF FF 7F F8 FF FF 7F 74  ..thk2S........t
0070: 68 6B 32 1C 07 80 66 05  80 F8 FF FF 7F F8 FF FF  hk2...f.........
0080: 7F 64 69 73 30 1D 08 80  23 53 F8 FF FF 7F F8 FF  .dis0...#S......
0090: FF 7F 64 69 73 30 39 09  80 6F 70 66 0A 80 F8 FF  ..dis09..opf....
00A0: FF 7F F8 FF FF 7F 75 74  6C 30 1D 0B 80 23 53 F8  ......utl0...#S.
00B0: FF FF 7F F8 FF FF 7F 75  74 6C 30 66 0A 80 F8 FF  .......utl0f....
00C0: FF 7F F8 FF FF 7F 75 74  6C 31 53 F8 FF FF 7F F8  ......utl1S.....
00D0: FF FF 7F 75 74 6C 31 32  0C 80 1F 00 0D 80 0E 80  ...utl12........
00E0: 0F 80 1F 01 22 01 2F 01  22 90 0F 01 00           ...."./."....   
```

#### Opcodes

```
  0: 0x004A [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk1" with entities [EventEntity, EventEntity]
  1: 0x0057 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=10*
  2: 0x0066 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk2" with entities [EventEntity, EventEntity]
  3: 0x0073 [0x1C] WAIT(60* ticks)
  4: 0x0076 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "dis0" with entities [EventEntity, EventEntity], work=10*
  5: 0x0085 [0x1D] PRINT_EVENT_MESSAGE(message_id=6979*)
    → "Mother! How long have you been saying that!?"
  6: 0x0088 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0089 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "dis0" with entities [EventEntity, EventEntity]
  8: 0x0096 [0x39] SET_ENTITY_DIRECTION(direction=15.7°*)
  9: 0x0099 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 10: 0x009A [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
 11: 0x009B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "utl0" with entities [EventEntity, EventEntity], work=11*
 12: 0x00AA [0x1D] PRINT_EVENT_MESSAGE(message_id=6980*)
    → "Just stop it! I don't want to hear it anymore!"
 13: 0x00AD [0x23] WAIT_FOR_DIALOG_INTERACTION
 14: 0x00AE [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "utl0" with entities [EventEntity, EventEntity]
 15: 0x00BB [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "utl1" with entities [EventEntity, EventEntity], work=11*
 16: 0x00CA [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "utl1" with entities [EventEntity, EventEntity]
 17: 0x00D7 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
 18: 0x00DA [0x1F] MOVE_ENTITY: EventEntity moves to X=17.262*, Z=45.558*, Y=-8.008*
 19: 0x00E2 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
 20: 0x00E4 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
 21: 0x00E6 [0x2F] Celestina (ID: 17797154/0x010F9022)->Render.Flags0 |= 0x80000 // Bit 19
 22: 0x00EC [0x00] END_REQSTACK()
```
