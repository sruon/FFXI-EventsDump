# 16904368 - Justinius

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Monarch Linn (ID: 31) |
| Block Size       | 104 bytes             |
| Total Events     | 3                     |
| References Count | 8                     |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      9 |              3 |
| [32001](#event-32001)    | 0x0009       |     10 |              2 |
| [65535.1](#event-655351) | 0x0013       |     24 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x9B52B     |      636203 |
|       1 | 0x92ACE     |      600782 |
|       2 | 0xFA09      |       64009 |
|       3 | 0x0838      |        2104 |
|       4 | 0x0028      |          40 |
|       5 | 0x9A17E     |      631166 |
|       6 | 0x92A3A     |      600634 |
|       7 | 0xFABA      |       64186 |

## Events

### Event 65535

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0000  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 92 01 F8 FF FF 7F 33 01  00                       ......3..       
```

#### Opcodes

```
  0: 0x0000 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0006 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  2: 0x0008 [0x00] END_REQSTACK()
```

### Event 32001

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0009   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                             37 00 80 01 80 02 80           7......
0010: 03 80 00                                          ...             
```

#### Opcodes

```
  0: 0x0009 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=636.203*, z=600.782*, y=64.009*, direction=184.9°*
  1: 0x0012 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0013   |
| Data Size    | 24 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:          79 00 F8 FF FF  7F A5 F0 01 01 32 04 80     y.........2..
0020: 1F 00 05 80 06 80 07 80  1F 01 00                 ...........     
```

#### Opcodes

```
  0: 0x0013 [0x79] EventEntity looks at Bahamut (ID: 16904357/0x0101F0A5) (Basic look)
  1: 0x001D [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  2: 0x0020 [0x1F] MOVE_ENTITY: EventEntity moves to X=631.166*, Z=600.634*, Y=64.186*
  3: 0x0028 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x002A [0x00] END_REQSTACK()
```
