# 16908463 - Shikaree Y

## Common Data

| Field            | Value                  |
|------------------|------------------------|
| Zone             | Sealion's Den (ID: 32) |
| Block Size       | 172 bytes              |
| Total Events     | 5                      |
| References Count | 17                     |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |     13 |              3 |
| [15](#event-15)          | 0x000D       |     10 |              2 |
| [65535.1](#event-655351) | 0x0017       |     24 |              6 |
| [32000](#event-32000)    | 0x002F       |      1 |              1 |
| [65535.2](#event-655352) | 0x0030       |     19 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x96682     |      616066 |
|       1 | 0xBD261     |      774753 |
|       2 | 0x20666     |      132710 |
|       3 | 0x07F1      |        2033 |
|       4 | 0x000D      |          13 |
|       5 | 0x9576D     |      612205 |
|       6 | 0xBB920     |      768288 |
|       7 | 0x20645     |      132677 |
|       8 | 0x93E2C     |      605740 |
|       9 | 0xB98AD     |      759981 |
|      10 | 0x20C91     |      134289 |
|      11 | 0x0000      |           0 |
|      12 | 0x0001      |           1 |
|      13 | 0xFFF40D8D  |  4294184333 |
|      14 | 0xFFFEDEED  |  4294893293 |
|      15 | 0xFFFE6C4D  |  4294863949 |
|      16 | 0x0C8B      |        3211 |

## Events

### Event 65535

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0000   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 94 00 F8 FF FF 7F 92 01  F8 FF FF 7F 00           .............   
```

#### Opcodes

```
  0: 0x0000 [0x94] EventEntity->Render.Flags3 = Flags3  // No change (flag=0)
  1: 0x0006 [0x92] EventEntity->Render.Flags3 ^= 0x01
  2: 0x000C [0x00] END_REQSTACK()
```

### Event 15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000D   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                         37 00 80               7..
0010: 01 80 02 80 03 80 00                              .......         
```

#### Opcodes

```
  0: 0x000D [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=616.066*, z=774.753*, y=132.710*, direction=178.7°*
  1: 0x0016 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0017   |
| Data Size    | 24 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                      32  04 80 1F 00 05 80 06 80         2........
0020: 07 80 1F 01 1F 00 08 80  09 80 0A 80 1F 01 00     ............... 
```

#### Opcodes

```
  0: 0x0017 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x001A [0x1F] MOVE_ENTITY: EventEntity moves to X=612.205*, Z=768.288*, Y=132.677*
  2: 0x0022 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0024 [0x1F] MOVE_ENTITY: EventEntity moves to X=605.740*, Z=759.981*, Y=134.289*
  4: 0x002C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x002E [0x00] END_REQSTACK()
```

### Event 32000

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x002F  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                               00                 .
```

#### Opcodes

```
  0: 0x002F [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0030   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030: 6C F8 FF FF 7F 0B 80 0C  80 37 0D 80 0E 80 0F 80  l........7......
0040: 10 80 00                                          ...             
```

#### Opcodes

```
  0: 0x0030 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  1: 0x0039 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-782.963*, z=-74.003*, y=-103.347*, direction=282.2°*
  2: 0x0042 [0x00] END_REQSTACK()
```
