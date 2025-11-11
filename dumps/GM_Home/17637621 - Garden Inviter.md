# 17637621 - Garden Inviter

## Common Data

| Field            | Value             |
|------------------|-------------------|
| Zone             | GM_Home (ID: 210) |
| Block Size       | 132 bytes         |
| Total Events     | 2                 |
| References Count | 6                 |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [175](#event-175)     | 0x0001       |     80 |             21 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0xFFFFFFFF  |  4294967295 |
|       2 | 0x0001      |           1 |
|       3 | 0x23B2      |        9138 |
|       4 | 0x23B3      |        9139 |
|       5 | 0x23B4      |        9140 |

## String References

- **9138**: Visit whose Mog Garden? [No one's./%1's./%2's./%3's./%4's./%5's./%6's./%7's./%8's./%9's./%10's./%11's./%12's./%13's./%14's./%15's./%16's./%17's.]
- **9139**: You decided you have better things to do.
- **9140**: Commencing transportation to the selected individual's Mog Garden.

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

### Event 175

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 80 bytes |
| Instructions | 21       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    C2 01 00 00 02 00 00  00 80 01 4C 00 1E F0 FF   ..........L....
0010: FF 7F C2 01 00 00 0F 00  00 01 80 3D 00 00 00 80  ...........=....
0020: 02 80 24 03 80 00 80 00  00 25 02 00 10 00 80 00  ..$......%......
0030: 3E 00 1D 04 80 23 03 01  10 00 80 01 49 00 42 1D  >....#......I.B.
0040: 05 80 23 C2 02 00 10 01  10 01 4F 00 06 01 10 21  ..#.......O....!
0050: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0xC2] PARTY_STATE_CHECK: ExtData[1]->WorkLocal[0] = mask of visitable party members
  1: 0x0005 [0x02] IF !(ExtData[1]->WorkLocal[0] == 0*) GOTO 0x004C
  2: 0x000D [0x1E] EventEntity looks at LocalPlayer and starts talking
  3: 0x0012 [0xC2] PARTY_STATE_CHECK: ExtData[1]->WorkLocal[0] = mask of visitable party members
  4: 0x0016 [0x0F] ExtData[1]->WorkLocal[0] ^= 4294967295*
  5: 0x001B [0x3D] CLEAR_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[0], bit_index_work_offset=0*, condition_work_offset=1*)
  6: 0x0022 [0x24] CREATE_DIALOG(message_id=9138*, default_option=0*, option_flags=ExtData[1]->WorkLocal[0])
    → "Visit whose Mog Garden? [No one's./%1's./%2's./%3's./%4's./%5's./%6's./%7's./%8's./%9's./%10's./%11's./%12's./%13's./%14's./%15's./%16's./%17's.]"
  7: 0x0029 [0x25] WAIT_DIALOG_SELECT()
  8: 0x002A [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x003E
  9: 0x0032 [0x1D] PRINT_EVENT_MESSAGE(message_id=9139*)
    → "You decided you have better things to do."
 10: 0x0035 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x0036 [0x03] Work_Zone[1] = 0*
 12: 0x003B [0x01] GOTO 0x0049
 13: 0x003E [0x42] SET_CLI_EVENT_CANCEL_DATA()
 14: 0x003F [0x1D] PRINT_EVENT_MESSAGE(message_id=9140*)
    → "Commencing transportation to the selected individual's Mog Garden."
 15: 0x0042 [0x23] WAIT_FOR_DIALOG_INTERACTION
 16: 0x0043 [0xC2] PARTY_STATE_CHECK: Work_Zone[1] = check if party member (from Work_Zone[0]) house is open

SUBROUTINE_0049:
 17: 0x0049 [0x01] GOTO 0x004F
 18: 0x004C [0x06] Work_Zone[1] = 0

SUBROUTINE_004F:
 19: 0x004F [0x21] END_EVENT
 20: 0x0050 [0x00] END_REQSTACK()
```
