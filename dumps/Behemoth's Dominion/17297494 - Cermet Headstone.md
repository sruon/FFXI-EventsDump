# 17297494 - Cermet Headstone

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Behemoth's Dominion (ID: 127) |
| Block Size       | 124 bytes                     |
| Total Events     | 3                             |
| References Count | 4                             |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [200](#event-200)     | 0x0001       |     39 |             10 |
| [201](#event-201)     | 0x0028       |     39 |             10 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1CA7      |        7335 |
|       1 | 0x1CA8      |        7336 |
|       2 | 0x0000      |           0 |
|       3 | 0x0001      |           1 |

## String References

- **7335**: 6... A single fragment of light. The way in which it shines suggests that it is resonating with something...
- **7336**: Do you remove the $3? [Yes./No.]

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

### Event 200

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 39 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    4A F0 FF FF 7F F8 FF  FF 7F 48 00 80 23 24 01   J........H..#$.
0010: 80 02 80 02 80 25 02 00  10 02 80 00 26 00 03 01  .....%......&...
0020: 10 03 80 01 26 00 21 00                           ....&.!.        
```

#### Opcodes

```
  0: 0x0001 [0x4A] LocalPlayer looks at EventEntity
  1: 0x000A [0x48] [System] [7335*]:
    → "6... A single fragment of light. The way in which it shines suggests that it is resonating with something..."
  2: 0x000D [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x000E [0x24] CREATE_DIALOG(message_id=7336*, default_option=0*, option_flags=0*)
    → "Do you remove the $3? [Yes./No.]"
  4: 0x0015 [0x25] WAIT_DIALOG_SELECT()
  5: 0x0016 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0026
  6: 0x001E [0x03] Work_Zone[1] = 1*
  7: 0x0023 [0x01] GOTO 0x0026

SUBROUTINE_0026:
  8: 0x0026 [0x21] END_EVENT
  9: 0x0027 [0x00] END_REQSTACK()
```

### Event 201

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0028   |
| Data Size    | 39 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                          4A F0 FF FF 7F F8 FF FF          J.......
0030: 7F 48 00 80 23 24 01 80  02 80 02 80 25 02 00 10  .H..#$......%...
0040: 02 80 00 4D 00 03 01 10  03 80 01 4D 00 21 00     ...M.......M.!. 
```

#### Opcodes

```
  0: 0x0028 [0x4A] LocalPlayer looks at EventEntity
  1: 0x0031 [0x48] [System] [7335*]:
    → "6... A single fragment of light. The way in which it shines suggests that it is resonating with something..."
  2: 0x0034 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0035 [0x24] CREATE_DIALOG(message_id=7336*, default_option=0*, option_flags=0*)
    → "Do you remove the $3? [Yes./No.]"
  4: 0x003C [0x25] WAIT_DIALOG_SELECT()
  5: 0x003D [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x004D
  6: 0x0045 [0x03] Work_Zone[1] = 1*
  7: 0x004A [0x01] GOTO 0x004D

SUBROUTINE_004D:
  8: 0x004D [0x21] END_EVENT
  9: 0x004E [0x00] END_REQSTACK()
```
