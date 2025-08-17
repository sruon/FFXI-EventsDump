# 17666742 - Watergrass

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Abyssea - Vunkerl (ID: 217) |
| Block Size       | 140 bytes                   |
| Total Events     | 3                           |
| References Count | 7                           |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [1034](#event-1034)   | 0x0001       |     21 |              7 |
| [1035](#event-1035)   | 0x0016       |     62 |             17 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1FE9      |        8169 |
|       1 | 0x0000      |           0 |
|       2 | 0x1FFB      |        8187 |
|       3 | 0x0001      |           1 |
|       4 | 0x1FFC      |        8188 |
|       5 | 0x0002      |           2 |
|       6 | 0x1FFD      |        8189 |

## String References

- **8169**: You pluck a handful of watergrass from the ground.
- **8187**: The leaves are covered with beads of rainwater...
- **8188**: The leaves are coated with a thin layer of what appears to be gunpowder...
- **8189**: A curious liquid oozes from the plant's stalk...

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

### Event 1034

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 21 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    42 29 05 F0 FF FF 7F  07 48 00 80 23 29 05 F0   B)......H..#)..
0010: FF FF 7F 08 21 00                                 ....!.          
```

#### Opcodes

```
  0: 0x0001 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0002 [0x29] REQ_SET_WAIT(priority=0x05, entity_id=LocalPlayer, tag_num=0x07)
  2: 0x0009 [0x48] [System] [8169*]:
    → "You pluck a handful of watergrass from the ground."
  3: 0x000C [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x000D [0x29] REQ_SET_WAIT(priority=0x05, entity_id=LocalPlayer, tag_num=0x08)
  5: 0x0014 [0x21] END_EVENT
  6: 0x0015 [0x00] END_REQSTACK()
```

### Event 1035

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0016   |
| Data Size    | 62 bytes |
| Instructions | 17       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                   42 29  05 F0 FF FF 7F 07 02 02        B)........
0020: 10 01 80 80 2D 00 48 02  80 23 01 4B 00 02 02 10  ....-.H..#.K....
0030: 03 80 80 3C 00 48 04 80  23 01 4B 00 02 02 10 05  ...<.H..#.K.....
0040: 80 80 4B 00 48 06 80 23  01 4B 00 29 05 F0 FF FF  ..K.H..#.K.)....
0050: 7F 08 21 00                                       ..!.            
```

#### Opcodes

```
  0: 0x0016 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0017 [0x29] REQ_SET_WAIT(priority=0x05, entity_id=LocalPlayer, tag_num=0x07)
  2: 0x001E [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x002D
  3: 0x0026 [0x48] [System] [8187*]:
    → "The leaves are covered with beads of rainwater..."
  4: 0x0029 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x002A [0x01] GOTO 0x004B
  6: 0x002D [0x02] IF !(Work_Zone[2] == 1*) GOTO 0x003C
  7: 0x0035 [0x48] [System] [8188*]:
    → "The leaves are coated with a thin layer of what appears to be gunpowder..."
  8: 0x0038 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0039 [0x01] GOTO 0x004B
 10: 0x003C [0x02] IF !(Work_Zone[2] == 2*) GOTO 0x004B
 11: 0x0044 [0x48] [System] [8189*]:
    → "A curious liquid oozes from the plant's stalk..."
 12: 0x0047 [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x0048 [0x01] GOTO 0x004B

SUBROUTINE_004B:
 14: 0x004B [0x29] REQ_SET_WAIT(priority=0x05, entity_id=LocalPlayer, tag_num=0x08)
 15: 0x0052 [0x21] END_EVENT
 16: 0x0053 [0x00] END_REQSTACK()
```
