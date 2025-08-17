# 17122231 - Cait Sith Tri

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Batallia Downs [S] (ID: 84) |
| Block Size       | 116 bytes                   |
| Total Events     | 3                           |
| References Count | 4                           |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [21](#event-21)          | 0x0001       |      3 |              2 |
| [65535.1](#event-655351) | 0x0004       |     67 |             13 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0003      |           3 |
|       1 | 0x0040      |          64 |
|       2 | 0x0001      |           1 |
|       3 | 0x0800      |        2048 |

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

### Event 21

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 3 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    33 01 00                                        3..            
```

#### Opcodes

```
  0: 0x0001 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  1: 0x0003 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0004   |
| Data Size    | 67 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:             33 01 3B F8  FF FF 7F 00 00 01 00 02      3.;.........
0010: 00 06 05 00 16 04 00 05  00 00 80 07 02 00 04 00  ................
0020: 3A F8 FF FF 7F 03 00 37  00 00 01 00 02 00 03 00  :......7........
0030: 07 05 00 01 80 1C 02 80  01 14 00 02 05 00 03 80  ................
0040: 04 46 00 06 05 00 00                              .F.....         
```

#### Opcodes

```
  0: 0x0004 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  1: 0x0006 [0x3B] GET_ENTITY_POSITION(entity=EventEntity, x_destination=ExtData[1]->WorkLocal[0], y_destination=ExtData[1]->WorkLocal[1], z_destination=ExtData[1]->WorkLocal[2])
  2: 0x0011 [0x06] ExtData[1]->WorkLocal[5] = 0
  3: 0x0014 [0x16] ExtData[1]->WorkLocal[4] = sin(ExtData[1]->WorkLocal[5]) * 3*
  4: 0x001B [0x07] ExtData[1]->WorkLocal[2] += ExtData[1]->WorkLocal[4]
  5: 0x0020 [0x3A] CONVERT_YAW_TO_BYTE(entity=EventEntity, result_destination=ExtData[1]->WorkLocal[3])
  6: 0x0027 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=ExtData[1]->WorkLocal[0], z=ExtData[1]->WorkLocal[1], y=ExtData[1]->WorkLocal[2], direction=ExtData[1]->WorkLocal[3]
  7: 0x0030 [0x07] ExtData[1]->WorkLocal[5] += 64*
  8: 0x0035 [0x1C] WAIT(1* ticks)
  9: 0x0038 [0x01] GOTO 0x0014
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x003B [0x02] IF !(ExtData[1]->WorkLocal[5] < 2048*) GOTO 0x0046
     0x0043 [0x06] ExtData[1]->WorkLocal[5] = 0
     0x0046 [0x00] END_REQSTACK()
```
