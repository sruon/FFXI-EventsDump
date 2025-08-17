# 17613269 - Geomantic Reservoir

## Common Data

| Field            | Value             |
|------------------|-------------------|
| Zone             | Fei'Yin (ID: 204) |
| Block Size       | 244 bytes         |
| Total Events     | 3                 |
| References Count | 11                |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [15000](#event-15000) | 0x0001       |    155 |             35 |
| [15002](#event-15002) | 0x009C       |     13 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x000D      |          13 |
|       2 | 0x29A6      |       10662 |
|       3 | 0x002D      |          45 |
|       4 | 0x29A7      |       10663 |
|       5 | 0x001E      |          30 |
|       6 | 0x29A5      |       10661 |
|       7 | 0x8CA0      |       36000 |
|       8 | 0x29A8      |       10664 |
|       9 | 0x00B4      |         180 |
|      10 | 0x0710      |        1808 |

## String References

- **10661**: 
- **10662**: You are assaulted by an uncanny sensation.
- **10663**: The arcane energies begin to course within your veins.
- **10664**: You feel a mystical warmth welling up inside you!

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

### Event 15000

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 155 bytes |
| Instructions | 35        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    42 03 00 00 00 80 03  05 00 00 80 03 01 00 00   B..............
0010: 80 03 04 00 00 80 03 02  00 01 80 03 03 00 02 10  ................
0020: 4A F0 FF FF 7F F8 FF FF  7F 6F 76 F0 FF FF 7F 48  J........ov....H
0030: 02 80 23 6E F0 FF FF 7F  03 80 99 F0 FF FF 7F 48  ..#n...........H
0040: 04 80 23 1C 05 80 03 02  10 03 00 28 10 D6 C1 0C  ..#........(....
0050: 01 02 28 10 D7 C1 0C 01  02 48 06 80 23 7A 00 D6  ..(......H..#z..
0060: C1 0C 01 7A 00 D7 C1 0C  01 28 10 D7 C1 0C 01 03  ...z.....(......
0070: 03 05 00 03 10 02 05 00  07 80 04 82 00 03 05 00  ................
0080: 07 80 48 08 80 23 AD 00  02 00 D5 C1 0C 01 F0 FF  ..H..#..........
0090: FF 7F 1C 09 80 03 01 10  05 00 21 00              ..........!.    
```

#### Opcodes

```
  0: 0x0001 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0002 [0x03] ExtData[1]->WorkLocal[0] = 0*
  2: 0x0007 [0x03] ExtData[1]->WorkLocal[5] = 0*
  3: 0x000C [0x03] ExtData[1]->WorkLocal[1] = 0*
  4: 0x0011 [0x03] ExtData[1]->WorkLocal[4] = 0*
  5: 0x0016 [0x03] ExtData[1]->WorkLocal[2] = 13*
  6: 0x001B [0x03] ExtData[1]->WorkLocal[3] = Work_Zone[2]
  7: 0x0020 [0x4A] LocalPlayer looks at EventEntity
  8: 0x0029 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  9: 0x002A [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until LocalPlayer Render.Flags0 and Render.Flags3 conditions are met
 10: 0x002F [0x48] [System] [10662*]:
    → "You are assaulted by an uncanny sensation."
 11: 0x0032 [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x0033 [0x6E] LocalPlayer uses emote 45*
 13: 0x003A [0x99] Wait for LocalPlayer animation to complete
 14: 0x003F [0x48] [System] [10663*]:
    → "The arcane energies begin to course within your veins."
 15: 0x0042 [0x23] WAIT_FOR_DIALOG_INTERACTION
 16: 0x0043 [0x1C] WAIT(30* ticks)
 17: 0x0046 [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[3]
 18: 0x004B [0x28] REQ_SET_WITH_CONDITIONS(priority=0x10, target_entity=Unknown NPC (ID: 17613270/0x010CC1D6), tag_num=0x02)
 19: 0x0052 [0x28] REQ_SET_WITH_CONDITIONS(priority=0x10, target_entity=Unknown NPC (ID: 17613271/0x010CC1D7), tag_num=0x02)
 20: 0x0059 [0x48] [System] [10661*]:
    → ""
 21: 0x005C [0x23] WAIT_FOR_DIALOG_INTERACTION
 22: 0x005D [0x7A] VM_CONTROL: Reset VM for Unknown NPC (ID: 17613270/0x010CC1D6)
 23: 0x0063 [0x7A] VM_CONTROL: Reset VM for Unknown NPC (ID: 17613271/0x010CC1D7)
 24: 0x0069 [0x28] REQ_SET_WITH_CONDITIONS(priority=0x10, target_entity=Unknown NPC (ID: 17613271/0x010CC1D7), tag_num=0x03)
 25: 0x0070 [0x03] ExtData[1]->WorkLocal[5] = Work_Zone[3]
 26: 0x0075 [0x02] IF !(ExtData[1]->WorkLocal[5] < 36000*) GOTO 0x0082
 27: 0x007D [0x03] ExtData[1]->WorkLocal[5] = 36000*
 28: 0x0082 [0x48] [System] [10664*]:
    → "You feel a mystical warmth welling up inside you!"
 29: 0x0085 [0x23] WAIT_FOR_DIALOG_INTERACTION
 30: 0x0086 [0xAD] DUAL_ENTITY_SCHEDULER_HANDLER: Execute sub-case 0 with entities [Geomantic Reservoir (ID: 17613269/0x010CC1D5), LocalPlayer], work=ExtData[1]->WorkLocal[2]
 31: 0x0092 [0x1C] WAIT(180* ticks)
 32: 0x0095 [0x03] Work_Zone[1] = ExtData[1]->WorkLocal[5]
 33: 0x009A [0x21] END_EVENT
 34: 0x009B [0x00] END_REQSTACK()
```

### Event 15002

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009C   |
| Data Size    | 13 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                      C4 02 0A 80              ....
00A0: F0 FF FF 7F F0 FF FF 7F  00                       .........       
```

#### Opcodes

```
  0: 0x009C [0xC4] SCHEDULE_MAGIC_CASTING_ALT (arg=18): LocalPlayer casts magic 1808* on LocalPlayer
  1: 0x00A8 [0x00] END_REQSTACK()
```
